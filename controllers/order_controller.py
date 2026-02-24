"""Order controller with my-orders, place-order, admin-all, and status endpoints."""
import asyncio
import uuid
from datetime import datetime, date as DateType
from typing import List, Optional
from fastapi import Depends, Header, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session

from controllers.base_controller_impl import BaseControllerImpl
from schemas.order_schema import OrderSchema
from services.order_service import OrderService
from services.auth_service import decode_token
from services.email_service import (
    send_order_approved_email,
    send_order_canceled_email,
    send_order_in_progress_email,
    send_order_delivered_email,
    send_return_requested_email,
    send_return_contact_email,
)
from config.database import get_db, SessionLocal
from services.cache_service import cache_service
from models.order import OrderModel
from models.order_detail import OrderDetailModel
from models.address import AddressModel
from models.bill import BillModel
from models.product import ProductModel
from models.client import ClientModel
from models.enums import DeliveryMethod, Status, PaymentType


# ── Pydantic schemas ────────────────────────────────────────────────────────
class PlaceOrderItem(BaseModel):
    product_id: int
    quantity: int
    unit_price: float

class PlaceOrderAddress(BaseModel):
    street: str
    number: Optional[str] = ""
    city: str

class PlaceOrderRequest(BaseModel):
    items: List[PlaceOrderItem]
    address: PlaceOrderAddress
    payment_type: Optional[str] = "CASH"

class UpdateStatusRequest(BaseModel):
    status: str  # "PENDING" | "IN_PROGRESS" | "DELIVERED" | "CANCELED"
# ───────────────────────────────────────────────────────────────────────────

# Seconds to wait before auto-approving (0 = instant)
APPROVAL_DELAY = {
    "MERCADOPAGO":   0,
    "PAYPAL":        0,
    "DEBIT":         0,
    "CASH":          0,
    "CARD":          0,
    "CREDIT":        15,
    "BANK_TRANSFER": 30,
}

STATUS_MAP = {
    "PENDING":          Status.PENDING,
    "APPROVED":         Status.APPROVED,
    "IN_PROGRESS":      Status.IN_PROGRESS,
    "DELIVERED":        Status.DELIVERED,
    "CANCELED":         Status.CANCELED,
    "RETURN_REQUESTED": Status.RETURN_REQUESTED,
}


async def _approve_order_background(
    order_id, delay, client_email, client_name, bill_number,
    items_for_email, items_for_stock, subtotal, iva, total, address_str, payment_method,
):
    """Background task: optionally wait, set APPROVED, reduce stock, send email."""
    if delay > 0:
        await asyncio.sleep(delay)

    # Update DB: approve order and reduce stock
    db = SessionLocal()
    try:
        order = db.query(OrderModel).filter(OrderModel.id_key == order_id).first()
        if order and order.status == Status.PENDING:
            order.status = Status.APPROVED
            for item in items_for_stock:
                product = db.query(ProductModel).filter(ProductModel.id_key == item["product_id"]).first()
                if product:
                    product.stock -= item["quantity"]
                    print(f"[STOCK] Producto #{item['product_id']} stock reducido -{item['quantity']} → {product.stock}")
            db.commit()
            # Invalidate Redis cache for all affected products
            for item in items_for_stock:
                cache_service.delete(cache_service.build_key("products", "id", id=item["product_id"]))
            cache_service.delete_pattern("products:list:*")
            print(f"[ORDER] Orden #{order_id} aprobada ({payment_method})")
        else:
            print(f"[ORDER] Orden #{order_id} no encontrada o ya modificada")
    except Exception as e:
        db.rollback()
        print(f"[ORDER ERROR] Error aprobando #{order_id}: {e}")
    finally:
        db.close()

    # Send approval confirmation email
    try:
        await send_order_approved_email(
            to_email=client_email,
            client_name=client_name,
            order_id=order_id,
            bill_number=bill_number,
            items=items_for_email,
            subtotal=subtotal,
            iva=iva,
            total=total,
            address=address_str,
            payment_method=payment_method,
        )
    except Exception as e:
        print(f"[EMAIL WARNING] No se pudo enviar email de aprobacion: {e}")


class OrderController(BaseControllerImpl):
    """Controller for Order entity."""

    def __init__(self):
        super().__init__(
            schema=OrderSchema,
            service_factory=lambda db: OrderService(db),
            tags=["Orders"]
        )
        self._register_admin_routes()
        self._register_order_routes()

    def _register_admin_routes(self):

        # ── ADMIN: ALL ORDERS ──────────────────────────────────────────────
        @self.router.get("/admin-all/", status_code=status.HTTP_200_OK)
        async def admin_all_orders(
            authorization: str = Header(None),
            db: Session = Depends(get_db)
        ):
            """Admin only: return all orders with client info and details."""
            if not authorization or not authorization.startswith("Bearer "):
                raise HTTPException(status_code=401, detail="No autenticado")
            payload = decode_token(authorization[7:])
            if not payload or payload.get("role") != "admin":
                raise HTTPException(status_code=403, detail="Acceso denegado")

            orders = db.query(OrderModel).order_by(OrderModel.date.desc()).all()
            result = []
            for order in orders:
                client = db.query(ClientModel).filter(ClientModel.id_key == order.client_id).first()
                details = db.query(OrderDetailModel).filter(OrderDetailModel.order_id == order.id_key).all()
                bill = db.query(BillModel).filter(BillModel.id_key == order.bill_id).first()
                items = []
                for d in details:
                    product = db.query(ProductModel).filter(ProductModel.id_key == d.product_id).first()
                    items.append({
                        "product_id": d.product_id,
                        "name": product.name if product else "Producto eliminado",
                        "quantity": d.quantity,
                        "unit_price": d.price,
                        "image_path": product.image_path if product else None,
                    })
                result.append({
                    "id": order.id_key,
                    "date": order.date.isoformat() if order.date else None,
                    "total": order.total,
                    "status": order.status.name if order.status else "PENDING",
                    "client": {
                        "id": client.id_key if client else None,
                        "name": f"{client.name} {client.lastname}" if client else "Usuario eliminado",
                        "email": client.email if client else "",
                    },
                    "bill_number": bill.bill_number if bill else "",
                    "payment_type": bill.payment_type.name if bill and bill.payment_type else "",
                    "items": items,
                })
            return result

        # ── ADMIN: UPDATE ORDER STATUS ─────────────────────────────────────
        @self.router.patch("/{order_id}/status/", status_code=status.HTTP_200_OK)
        async def update_order_status(
            order_id: int,
            body: UpdateStatusRequest,
            authorization: str = Header(None),
            db: Session = Depends(get_db)
        ):
            """Admin only: change the status of an order."""
            if not authorization or not authorization.startswith("Bearer "):
                raise HTTPException(status_code=401, detail="No autenticado")
            payload = decode_token(authorization[7:])
            if not payload or payload.get("role") != "admin":
                raise HTTPException(status_code=403, detail="Acceso denegado")

            new_status_key = body.status.upper()
            if new_status_key not in STATUS_MAP:
                raise HTTPException(status_code=400, detail=f"Estado inválido: {body.status}")

            order = db.query(OrderModel).filter(OrderModel.id_key == order_id).first()
            if not order:
                raise HTTPException(status_code=404, detail="Orden no encontrada")

            # Forward-only flow: APPROVED → IN_PROGRESS → DELIVERED
            FORWARD_FLOW = {
                Status.APPROVED:    Status.IN_PROGRESS,
                Status.IN_PROGRESS: Status.DELIVERED,
            }
            allowed_next = FORWARD_FLOW.get(order.status)
            if STATUS_MAP[new_status_key] != allowed_next:
                raise HTTPException(
                    status_code=400,
                    detail=f"No se puede cambiar el estado de {order.status.name} a {new_status_key}. Solo se permite avanzar al siguiente estado."
                )

            order.status = STATUS_MAP[new_status_key]
            db.commit()
            db.refresh(order)

            # ── Send email notification for IN_PROGRESS / DELIVERED ──────────
            if new_status_key in ("IN_PROGRESS", "DELIVERED"):
                try:
                    client = db.query(ClientModel).filter(ClientModel.id_key == order.client_id).first()
                    bill = db.query(BillModel).filter(BillModel.id_key == order.bill_id).first()
                    details = db.query(OrderDetailModel).filter(OrderDetailModel.order_id == order.id_key).all()
                    if client and client.email:
                        items_for_email = []
                        for d in details:
                            product = db.query(ProductModel).filter(ProductModel.id_key == d.product_id).first()
                            items_for_email.append({
                                "name": product.name if product else f"Producto #{d.product_id}",
                                "quantity": d.quantity,
                                "unit_price": float(d.price),
                            })
                        subtotal = round(sum(i["quantity"] * i["unit_price"] for i in items_for_email), 2)
                        iva = round(subtotal * 0.21, 2)
                        total = round(subtotal + iva, 2)
                        payment_method = bill.payment_type.name if bill and bill.payment_type else "CASH"
                        client_name = f"{client.name} {client.lastname}".strip()
                        bill_number = bill.bill_number if bill else ""
                        if new_status_key == "IN_PROGRESS":
                            asyncio.create_task(send_order_in_progress_email(
                                to_email=client.email,
                                client_name=client_name,
                                order_id=order.id_key,
                                bill_number=bill_number,
                                items=items_for_email,
                                subtotal=subtotal,
                                iva=iva,
                                total=total,
                                payment_method=payment_method,
                            ))
                        else:
                            asyncio.create_task(send_order_delivered_email(
                                to_email=client.email,
                                client_name=client_name,
                                order_id=order.id_key,
                                bill_number=bill_number,
                                items=items_for_email,
                                subtotal=subtotal,
                                iva=iva,
                                total=total,
                                payment_method=payment_method,
                            ))
                except Exception as email_err:
                    print(f"[EMAIL WARNING] No se pudo enviar email de estado {new_status_key}: {email_err}")

            return {"order_id": order_id, "status": new_status_key, "message": "Estado actualizado"}


    def _register_order_routes(self):
        """Register order-specific routes."""

        @self.router.get("/my-orders/", status_code=status.HTTP_200_OK)
        async def my_orders(
            authorization: str = Header(None),
            db: Session = Depends(get_db)
        ):
            """Return all orders belonging to the authenticated user, enriched with items and bill info."""
            if not authorization or not authorization.startswith("Bearer "):
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="No autenticado")
            payload = decode_token(authorization[7:])
            if not payload:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")

            orders = db.query(OrderModel).filter(
                OrderModel.client_id == payload["id"]
            ).order_by(OrderModel.date.desc()).all()

            result = []
            for order in orders:
                bill = db.query(BillModel).filter(BillModel.id_key == order.bill_id).first()
                details = db.query(OrderDetailModel).filter(OrderDetailModel.order_id == order.id_key).all()
                items = []
                for d in details:
                    product = db.query(ProductModel).filter(ProductModel.id_key == d.product_id).first()
                    items.append({
                        "product_id": d.product_id,
                        "name": product.name if product else f"Producto #{d.product_id}",
                        "quantity": d.quantity,
                        "unit_price": d.price,
                        "image_path": product.image_path if product else None,
                    })
                subtotal = round(sum(i["unit_price"] * i["quantity"] for i in items), 2)
                iva = round(subtotal * 0.21, 2)
                result.append({
                    "id": order.id_key,
                    "date": order.date.isoformat() if order.date else None,
                    "total": order.total,
                    "subtotal": subtotal,
                    "iva": iva,
                    "status": order.status.name if order.status else "PENDING",
                    "bill_number": bill.bill_number if bill else "",
                    "payment_type": bill.payment_type.name if bill and bill.payment_type else "",
                    "items": items,
                })
            return result

        @self.router.post("/place/", status_code=status.HTTP_201_CREATED)
        async def place_order(
            body: PlaceOrderRequest,
            authorization: str = Header(None),
            db: Session = Depends(get_db)
        ):
            """
            Create order atomically — stock is NOT reduced here.
            A background task approves the order (instantly or with a delay)
            and reduces stock only when APPROVED.
            """
            if not authorization or not authorization.startswith("Bearer "):
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="No autenticado")
            payload = decode_token(authorization[7:])
            if not payload:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")
            client_id = payload["id"]

            if not body.items:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El carrito está vacío")

            try:
                payment_key = (body.payment_type or "CASH").upper()
                payment_map = {
                    "CASH":          PaymentType.CASH,
                    "CARD":          PaymentType.CARD,
                    "DEBIT":         PaymentType.DEBIT,
                    "CREDIT":        PaymentType.CREDIT,
                    "BANK_TRANSFER": PaymentType.BANK_TRANSFER,
                    "MERCADOPAGO":   PaymentType.MERCADOPAGO,
                    "PAYPAL":        PaymentType.PAYPAL,
                }
                payment = payment_map.get(payment_key, PaymentType.CASH)
                delay = APPROVAL_DELAY.get(payment_key, 0)

                subtotal = round(sum(item.quantity * item.unit_price for item in body.items), 2)
                iva = round(subtotal * 0.21, 2)
                total = round(subtotal + iva, 2)

                # Validate stock before creating anything
                for item in body.items:
                    product = db.query(ProductModel).filter(ProductModel.id_key == item.product_id).first()
                    if not product:
                        raise HTTPException(
                            status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Producto {item.product_id} no encontrado"
                        )
                    if product.stock < item.quantity:
                        raise HTTPException(
                            status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Stock insuficiente para '{product.name}' (disponible: {product.stock})"
                        )

                bill = BillModel(
                    bill_number=f"BILL-{uuid.uuid4().hex[:10].upper()}",
                    discount=0.0,
                    date=DateType.today(),
                    total=total,
                    payment_type=payment,
                    client_id=client_id,
                )
                db.add(bill)
                db.flush()

                address = AddressModel(
                    street=body.address.street,
                    number=body.address.number,
                    city=body.address.city,
                    client_id=client_id,
                )
                db.add(address)
                db.flush()

                # Order stays PENDING until background task approves it
                order = OrderModel(
                    date=datetime.utcnow(),
                    total=total,
                    delivery_method=DeliveryMethod.HOME_DELIVERY,
                    status=Status.PENDING,
                    client_id=client_id,
                    bill_id=bill.id_key,
                )
                db.add(order)
                db.flush()

                # Details — NO stock reduction here
                items_for_email = []
                items_for_stock = []
                for item in body.items:
                    product = db.query(ProductModel).filter(ProductModel.id_key == item.product_id).first()
                    detail = OrderDetailModel(
                        quantity=item.quantity,
                        price=item.unit_price,
                        order_id=order.id_key,
                        product_id=item.product_id,
                    )
                    db.add(detail)
                    items_for_email.append({
                        "name": product.name if product else f"Producto #{item.product_id}",
                        "quantity": item.quantity,
                        "unit_price": item.unit_price,
                    })
                    items_for_stock.append({
                        "product_id": item.product_id,
                        "quantity": item.quantity,
                    })

                db.commit()

                client = db.query(ClientModel).filter(ClientModel.id_key == client_id).first()
                client_email = client.email if client else ""
                client_name = f"{client.name} {client.lastname}".strip() if client else ""
                address_str = f"{body.address.street} {body.address.number}, {body.address.city}".strip(", ")

                # Launch background approval task
                if client_email:
                    asyncio.create_task(_approve_order_background(
                        order_id=order.id_key,
                        delay=delay,
                        client_email=client_email,
                        client_name=client_name,
                        bill_number=bill.bill_number,
                        items_for_email=items_for_email,
                        items_for_stock=items_for_stock,
                        subtotal=subtotal,
                        iva=iva,
                        total=total,
                        address_str=address_str,
                        payment_method=payment_key,
                    ))

                return {
                    "order_id": order.id_key,
                    "subtotal": subtotal,
                    "iva": iva,
                    "total": total,
                    "status": "PENDING",
                    "bill_number": bill.bill_number,
                    "message": "Orden creada exitosamente"
                }

            except HTTPException:
                db.rollback()
                raise
            except Exception as e:
                db.rollback()
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=f"Error al procesar la orden: {str(e)}"
                )

        # ── CANCEL ORDER (cliente) ───────────────────────────────────────
        @self.router.post("/{order_id}/cancel/", status_code=status.HTTP_200_OK)
        async def cancel_order(
            order_id: int,
            authorization: str = Header(None),
            db: Session = Depends(get_db)
        ):
            """Client cancels their own order (only if not yet DELIVERED).
            Restores stock if the order was already APPROVED or IN_PROGRESS."""
            if not authorization or not authorization.startswith("Bearer "):
                raise HTTPException(status_code=401, detail="No autenticado")
            payload = decode_token(authorization[7:])
            if not payload:
                raise HTTPException(status_code=401, detail="Token inválido")

            order = db.query(OrderModel).filter(OrderModel.id_key == order_id).first()
            if not order:
                raise HTTPException(status_code=404, detail="Orden no encontrada")
            if order.client_id != payload["id"]:
                raise HTTPException(status_code=403, detail="No autorizado")
            if order.status == Status.DELIVERED:
                raise HTTPException(
                    status_code=400,
                    detail="No se puede cancelar un pedido ya entregado. Si no estás conforme, solicitá una devolución."
                )
            if order.status in (Status.CANCELED, Status.RETURN_REQUESTED):
                raise HTTPException(status_code=400, detail="Este pedido ya fue cancelado o tiene una solicitud de devolución.")

            # Restore stock only if it was already reduced (APPROVED or IN_PROGRESS)
            affected_product_ids = []
            if order.status in (Status.APPROVED, Status.IN_PROGRESS):
                details = db.query(OrderDetailModel).filter(OrderDetailModel.order_id == order.id_key).all()
                for d in details:
                    product = db.query(ProductModel).filter(ProductModel.id_key == d.product_id).first()
                    if product:
                        product.stock += d.quantity
                        affected_product_ids.append(d.product_id)
                        print(f"[STOCK] Producto #{d.product_id} stock restaurado +{d.quantity} → {product.stock}")

            order.status = Status.CANCELED
            db.commit()
            # Invalidate Redis cache for all affected products
            for pid in affected_product_ids:
                cache_service.delete(cache_service.build_key("products", "id", id=pid))
            if affected_product_ids:
                cache_service.delete_pattern("products:list:*")
            print(f"[ORDER] Orden #{order_id} cancelada")

            # Send cancelation email with refund notice
            try:
                client = db.query(ClientModel).filter(ClientModel.id_key == order.client_id).first()
                bill = db.query(BillModel).filter(BillModel.id_key == order.bill_id).first()
                details = db.query(OrderDetailModel).filter(OrderDetailModel.order_id == order.id_key).all()
                if client and client.email:
                    items_for_email = []
                    for d in details:
                        product = db.query(ProductModel).filter(ProductModel.id_key == d.product_id).first()
                        items_for_email.append({
                            "name": product.name if product else f"Producto #{d.product_id}",
                            "quantity": d.quantity,
                            "unit_price": float(d.price),
                        })
                    subtotal_e = round(sum(i["quantity"] * i["unit_price"] for i in items_for_email), 2)
                    iva_e = round(subtotal_e * 0.21, 2)
                    total_e = round(subtotal_e + iva_e, 2)
                    payment_method_e = bill.payment_type.name if bill and bill.payment_type else "CASH"
                    asyncio.create_task(send_order_canceled_email(
                        to_email=client.email,
                        client_name=f"{client.name} {client.lastname}".strip(),
                        order_id=order.id_key,
                        bill_number=bill.bill_number if bill else "",
                        items=items_for_email,
                        subtotal=subtotal_e,
                        iva=iva_e,
                        total=total_e,
                        payment_method=payment_method_e,
                    ))
            except Exception as email_err:
                print(f"[EMAIL WARNING] No se pudo enviar email de cancelación: {email_err}")

            return {"message": "Pedido cancelado exitosamente"}

        # ── REQUEST RETURN (cliente) ────────────────────────────────────
        @self.router.post("/{order_id}/return/", status_code=status.HTTP_200_OK)
        async def request_return(
            order_id: int,
            authorization: str = Header(None),
            db: Session = Depends(get_db)
        ):
            """Client requests a return for a delivered order."""
            if not authorization or not authorization.startswith("Bearer "):
                raise HTTPException(status_code=401, detail="No autenticado")
            payload = decode_token(authorization[7:])
            if not payload:
                raise HTTPException(status_code=401, detail="Token inválido")

            order = db.query(OrderModel).filter(OrderModel.id_key == order_id).first()
            if not order:
                raise HTTPException(status_code=404, detail="Orden no encontrada")
            if order.client_id != payload["id"]:
                raise HTTPException(status_code=403, detail="No autorizado")
            if order.status != Status.DELIVERED:
                raise HTTPException(
                    status_code=400,
                    detail="Solo se puede solicitar devolución de pedidos ya entregados."
                )

            order.status = Status.RETURN_REQUESTED
            db.commit()

            # Send return confirmation email to user
            try:
                client = db.query(ClientModel).filter(ClientModel.id_key == order.client_id).first()
                bill = db.query(BillModel).filter(BillModel.id_key == order.bill_id).first()
                if client and client.email:
                    asyncio.create_task(send_return_requested_email(
                        to_email=client.email,
                        client_name=f"{client.name} {client.lastname}".strip(),
                        order_id=order.id_key,
                        bill_number=bill.bill_number if bill else "",
                    ))
            except Exception as email_err:
                print(f"[EMAIL WARNING] No se pudo enviar email de devolución: {email_err}")

            return {"message": "Solicitud de devolución enviada. Nos pondremos en contacto a la brevedad."}

        # ── ADMIN: CONTACT USER FOR RETURN ─────────────────────────────
        @self.router.post("/{order_id}/contact-return/", status_code=status.HTTP_200_OK)
        async def admin_contact_return(
            order_id: int,
            authorization: str = Header(None),
            db: Session = Depends(get_db)
        ):
            """Admin sends return instructions email to the user."""
            if not authorization or not authorization.startswith("Bearer "):
                raise HTTPException(status_code=401, detail="No autenticado")
            payload = decode_token(authorization[7:])
            if not payload or payload.get("role") != "admin":
                raise HTTPException(status_code=403, detail="Acceso denegado")

            order = db.query(OrderModel).filter(OrderModel.id_key == order_id).first()
            if not order:
                raise HTTPException(status_code=404, detail="Orden no encontrada")
            if order.status != Status.RETURN_REQUESTED:
                raise HTTPException(status_code=400, detail="El pedido no tiene una solicitud de devolución activa.")

            client = db.query(ClientModel).filter(ClientModel.id_key == order.client_id).first()
            bill = db.query(BillModel).filter(BillModel.id_key == order.bill_id).first()
            if not client or not client.email:
                raise HTTPException(status_code=404, detail="No se encontró el email del cliente.")

            asyncio.create_task(send_return_contact_email(
                to_email=client.email,
                client_name=f"{client.name} {client.lastname}".strip(),
                order_id=order.id_key,
                bill_number=bill.bill_number if bill else "",
            ))
            return {"message": "Email de instrucciones de devolución enviado al usuario."}
