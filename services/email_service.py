"""Email service using fastapi-mail for order confirmations."""
import os
from typing import List
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import EmailStr


def get_mail_config() -> ConnectionConfig:
    return ConnectionConfig(
        MAIL_USERNAME=os.getenv("MAIL_USERNAME", ""),
        MAIL_PASSWORD=os.getenv("MAIL_PASSWORD", ""),
        MAIL_FROM=os.getenv("MAIL_FROM", os.getenv("MAIL_USERNAME", "")),
        MAIL_PORT=int(os.getenv("MAIL_PORT", "587")),
        MAIL_SERVER=os.getenv("MAIL_SERVER", "smtp.gmail.com"),
        MAIL_STARTTLS=True,
        MAIL_SSL_TLS=False,
        USE_CREDENTIALS=True,
        VALIDATE_CERTS=True,
    )


async def send_order_confirmation(
    to_email: str,
    client_name: str,
    order_id: int,
    bill_number: str,
    items: list,
    subtotal: float,
    iva: float,
    total: float,
    address: str,
    payment_method: str,
):
    """Send HTML order confirmation email to user."""
    # Build items rows
    rows = ""
    for item in items:
        subtotal_item = item["quantity"] * item["unit_price"]
        rows += f"""
        <tr>
          <td style="padding:8px 12px;border-bottom:1px solid #eee;">{item['name']}</td>
          <td style="padding:8px 12px;border-bottom:1px solid #eee;text-align:center;">{item['quantity']}</td>
          <td style="padding:8px 12px;border-bottom:1px solid #eee;text-align:right;">
            ${subtotal_item:,.2f}
          </td>
        </tr>
        """

    payment_labels = {
        "MERCADOPAGO": "MercadoPago",
        "BANK_TRANSFER": "Transferencia Bancaria",
        "PAYPAL": "PayPal",
        "CREDIT": "Tarjeta de Crédito",
        "DEBIT": "Tarjeta de Débito",
        "CARD": "Tarjeta",
        "CASH": "Efectivo",
    }
    payment_label = payment_labels.get(payment_method.upper(), payment_method)

    html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="color-scheme" content="light">
      <meta name="supported-color-schemes" content="light">
      <style>
        :root {{ color-scheme: light; }}
        body {{ font-family: Arial, sans-serif; background:#f4f4f4; margin:0; padding:0; }}
        .container {{ max-width:600px; margin:30px auto; background:#fff; border-radius:12px;
                      overflow:hidden; box-shadow:0 2px 12px rgba(0,0,0,0.08); }}
        .header {{ background: linear-gradient(to bottom,#79edd6,#a5efa2);
                   padding:32px; text-align:center; }}
        .header h1 {{ margin:0; font-size:28px; letter-spacing:-0.5px; color:#010101 !important; }}
        .header p {{ margin:6px 0 0; font-size:14px; color:#010101 !important; }}
        .body {{ padding:28px 32px; }}
        .order-box {{ background:#f9f9f9; border:1px solid #e5e5e5; border-radius:8px;
                      padding:16px 20px; margin-bottom:24px; }}
        .order-box p {{ margin:4px 0; font-size:14px; color:#555; }}
        .order-box strong {{ color:#1a1a1a; }}
        table {{ width:100%; border-collapse:collapse; margin-bottom:20px; font-size:14px; }}
        thead tr {{ background:#f3f4f6; }}
        thead th {{ padding:10px 12px; text-align:left; color:#555; font-weight:600; }}
        .totals {{ text-align:right; font-size:14px; margin-top:8px; }}
        .totals td {{ padding:4px 12px; }}
        .total-row td {{ font-size:17px; font-weight:bold; color:#6B21A8; padding-top:12px; }}
        .footer {{ background: linear-gradient(to bottom,#a5efa2,#79edd6); color:#010101 !important; text-align:center;
                   padding:20px; font-size:12px; }}
        .footer a {{ color:#1a4d18 !important; text-decoration:none; }}
      </style>
    </head>
    <body>
      <div class="container">
        <div class="header">
          <h1 style="color:#010101;">Beat<span style="color:#328c2f;">Hub</span><span style="color:#010101;">.ar</span></h1>
          <p>Confirmación de Compra</p>
        </div>
        <div class="body">
          <p style="font-size:16px;">¡Hola, <strong>{client_name}</strong>! 🎸</p>
          <p style="color:#555;font-size:14px;margin-top:0;">
            Tu orden fue recibida y está siendo procesada. Acá el detalle:
          </p>

          <div class="order-box">
            <p><strong>Número de Orden:</strong> #{order_id}</p>
            <p><strong>Factura:</strong> {bill_number}</p>
            <p><strong>Dirección de Envío:</strong> {address}</p>
            <p><strong>Método de Pago:</strong> {payment_label}</p>
          </div>

          <table>
            <thead>
              <tr>
                <th>Producto</th>
                <th style="text-align:center;">Cant.</th>
                <th style="text-align:right;">Subtotal</th>
              </tr>
            </thead>
            <tbody>
              {rows}
            </tbody>
          </table>

          <table class="totals">
            <tr>
              <td style="color:#555;">Subtotal (sin IVA):</td>
              <td><strong>${subtotal:,.2f}</strong></td>
            </tr>
            <tr>
              <td style="color:#555;">IVA (21%):</td>
              <td><strong>${iva:,.2f}</strong></td>
            </tr>
            <tr class="total-row">
              <td>Total:</td>
              <td>${total:,.2f}</td>
            </tr>
          </table>

          <p style="font-size:13px;color:#888;margin-top:16px;">
            Podés ver el estado de tu pedido en cualquier momento desde la sección
            <strong>Seguimiento</strong> de nuestra web.
          </p>
        </div>
        <div class="footer">
          <p>BeatHub.ar · Mendoza, Argentina</p>
          <p>Si tenés alguna consulta, contactanos al +549&nbsp;(3772)&nbsp;584894</p>
        </div>
      </div>
    </body>
    </html>
    """

    try:
        conf = get_mail_config()
        fm = FastMail(conf)
        message = MessageSchema(
            subject=f"BeatHub.ar — Confirmación de Orden #{order_id}",
            recipients=[to_email],
            body=html,
            subtype=MessageType.html,
        )
        await fm.send_message(message)
    except Exception as e:
        # Log but don't fail the order if email fails
        print(f"[EMAIL ERROR] No se pudo enviar confirmación a {to_email}: {e}")


async def send_payment_processing_email(
    to_email: str,
    client_name: str,
    bill_number: str,
    payment_label: str,
    delay_seconds: int,
):
    """Notify user that their payment is being processed (sent before the delay)."""
    minutes = delay_seconds // 60
    seconds = delay_seconds % 60
    if minutes > 0:
        tiempo = f"aproximadamente {minutes} minuto{'s' if minutes > 1 else ''}"
    else:
        tiempo = f"aproximadamente {seconds} segundos"

    html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="color-scheme" content="light">
      <meta name="supported-color-schemes" content="light">
      <style>:root{{color-scheme:light}}</style>
    </head>
    <body style="margin:0;padding:0;background:#f4f4f4;font-family:Arial,sans-serif">
      <div style="max-width:560px;margin:30px auto;background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 2px 12px rgba(0,0,0,.08)">
        <div style="background:linear-gradient(to bottom,#79edd6,#a5efa2);padding:32px;text-align:center">
          <h1 style="margin:0;font-size:28px;color:#010101 !important">Beat<span style="color:#328c2f !important">Hub</span><span style="color:#010101 !important">.ar</span></h1>
          <p style="margin:6px 0 0;font-size:14px;color:#010101 !important">⏳ Procesando tu pago</p>
        </div>
        <div style="padding:28px 32px">
          <p style="font-size:16px;color:#1a1a1a">Hola, <strong>{client_name}</strong> 👋</p>
          <p style="color:#555;font-size:14px">
            Recibimos tu compra. Tu pago con <strong>{payment_label}</strong> está siendo verificado.
          </p>
          <div style="background:#fef9c3;border:1px solid #fde047;border-radius:8px;padding:16px 20px;margin:20px 0">
            <p style="margin:0;font-size:14px;color:#713f12">
              🕐 El proceso tomará <strong>{tiempo}</strong>. Recibirás un segundo email cuando el pago sea confirmado.
            </p>
          </div>
          <div style="background:#f9f9f9;border:1px solid #e5e5e5;border-radius:8px;padding:14px 18px;margin-bottom:20px">
            <p style="margin:0;font-size:14px;color:#555"><strong>Factura:</strong> {bill_number}</p>
            <p style="margin:4px 0 0;font-size:14px;color:#555"><strong>Método:</strong> {payment_label}</p>
          </div>
          <p style="font-size:13px;color:#888">
            Podés seguir el estado de tu pedido en la sección <strong>Seguimiento</strong> de nuestra web.
          </p>
        </div>
        <div style="background:linear-gradient(to bottom,#a5efa2,#79edd6);padding:20px;text-align:center;color:#010101 !important;font-size:12px">
          <p style="margin:0">BeatHub.ar · Mendoza, Argentina</p>
        </div>
      </div>
    </body>
    </html>
    """

    try:
        conf = get_mail_config()
        fm = FastMail(conf)
        message = MessageSchema(
            subject=f"BeatHub.ar — Tu pago está siendo procesado ({bill_number})",
            recipients=[to_email],
            body=html,
            subtype=MessageType.html,
        )
        await fm.send_message(message)
    except Exception as e:
        print(f"[EMAIL ERROR] No se pudo enviar email de procesando a {to_email}: {e}")


async def send_order_approved_email(
    to_email: str,
    client_name: str,
    order_id: int,
    bill_number: str,
    items: list,
    subtotal: float,
    iva: float,
    total: float,
    address: str,
    payment_method: str,
):
    """Send HTML order approved email to user."""
    rows = ""
    for item in items:
        subtotal_item = item["quantity"] * item["unit_price"]
        rows += f"""
        <tr>
          <td style="padding:8px 12px;border-bottom:1px solid #eee;">{item['name']}</td>
          <td style="padding:8px 12px;border-bottom:1px solid #eee;text-align:center;">{item['quantity']}</td>
          <td style="padding:8px 12px;border-bottom:1px solid #eee;text-align:right;">${subtotal_item:,.2f}</td>
        </tr>
        """

    payment_labels = {
        "MERCADOPAGO": "MercadoPago",
        "BANK_TRANSFER": "Transferencia Bancaria",
        "PAYPAL": "PayPal",
        "CREDIT": "Tarjeta de Crédito",
        "DEBIT": "Tarjeta de Débito",
        "CARD": "Tarjeta",
        "CASH": "Efectivo",
    }
    payment_label = payment_labels.get(payment_method.upper(), payment_method)

    html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="color-scheme" content="light">
      <meta name="supported-color-schemes" content="light">
      <style>
        :root {{ color-scheme: light; }}
        body {{ font-family: Arial, sans-serif; background:#f4f4f4; margin:0; padding:0; }}
        .container {{ max-width:600px; margin:30px auto; background:#fff; border-radius:12px;
                      overflow:hidden; box-shadow:0 2px 12px rgba(0,0,0,0.08); }}
        .header {{ background: linear-gradient(to bottom,#79edd6,#a5efa2);
                   padding:32px; text-align:center; }}
        .header h1 {{ margin:0; font-size:28px; letter-spacing:-0.5px; color:#010101 !important; }}
        .header p {{ margin:6px 0 0; font-size:14px; color:#010101 !important; }}
        .body {{ padding:28px 32px; }}
        .order-box {{ background:#f9f9f9; border:1px solid #e5e5e5; border-radius:8px;
                      padding:16px 20px; margin-bottom:24px; }}
        .order-box p {{ margin:4px 0; font-size:14px; color:#555; }}
        .order-box strong {{ color:#1a1a1a; }}
        table {{ width:100%; border-collapse:collapse; margin-bottom:20px; font-size:14px; }}
        thead tr {{ background:#f3f4f6; }}
        thead th {{ padding:10px 12px; text-align:left; color:#555; font-weight:600; }}
        .totals {{ text-align:right; font-size:14px; margin-top:8px; }}
        .totals td {{ padding:4px 12px; }}
        .total-row td {{ font-size:17px; font-weight:bold; color:#1a7a2a; padding-top:12px; }}
        .footer {{ background: linear-gradient(to bottom,#a5efa2,#79edd6); color:#010101 !important;
                   text-align:center; padding:20px; font-size:12px; }}
      </style>
    </head>
    <body>
      <div class="container">
        <div class="header">
          <h1 style="color:#010101;">Beat<span style="color:#328c2f;">Hub</span><span style="color:#010101;">.ar</span></h1>
          <p>✅ ¡Pago Aprobado!</p>
        </div>
        <div class="body">
          <p style="font-size:16px;">¡Hola, <strong>{client_name}</strong>! 🎉</p>
          <p style="color:#555;font-size:14px;margin-top:0;">
            Tu pago fue <strong style="color:#1a7a2a;">aprobado</strong> y tu pedido está en preparación. Acá el detalle:
          </p>

          <div class="order-box">
            <p><strong>Número de Orden:</strong> #{order_id}</p>
            <p><strong>Factura:</strong> {bill_number}</p>
            <p><strong>Dirección de Envío:</strong> {address}</p>
            <p><strong>Método de Pago:</strong> {payment_label}</p>
          </div>

          <table>
            <thead>
              <tr>
                <th>Producto</th>
                <th style="text-align:center;">Cant.</th>
                <th style="text-align:right;">Subtotal</th>
              </tr>
            </thead>
            <tbody>
              {rows}
            </tbody>
          </table>

          <table class="totals">
            <tr>
              <td style="color:#555;">Subtotal (sin IVA):</td>
              <td><strong>${subtotal:,.2f}</strong></td>
            </tr>
            <tr>
              <td style="color:#555;">IVA (21%):</td>
              <td><strong>${iva:,.2f}</strong></td>
            </tr>
            <tr class="total-row">
              <td>Total:</td>
              <td>${total:,.2f}</td>
            </tr>
          </table>

          <p style="font-size:13px;color:#888;margin-top:16px;">
            Podés ver el estado de tu pedido en cualquier momento desde la sección
            <strong>Seguimiento</strong> de nuestra web.
          </p>
        </div>
        <div class="footer">
          <p>BeatHub.ar · Mendoza, Argentina</p>
          <p>Si tenés alguna consulta, contactanos al +549&nbsp;(3772)&nbsp;584894</p>
        </div>
      </div>
    </body>
    </html>
    """

    try:
        conf = get_mail_config()
        fm = FastMail(conf)
        message = MessageSchema(
            subject=f"BeatHub.ar — ✅ ¡Pago aprobado! Orden #{order_id}",
            recipients=[to_email],
            body=html,
            subtype=MessageType.html,
        )
        await fm.send_message(message)
    except Exception as e:
        print(f"[EMAIL ERROR] No se pudo enviar confirmación de aprobación a {to_email}: {e}")


async def send_order_canceled_email(
    to_email: str,
    client_name: str,
    order_id: int,
    bill_number: str,
    items: list,
    subtotal: float,
    iva: float,
    total: float,
    payment_method: str,
):
    """Notify user that their order has been canceled and funds will be refunded."""
    rows = ""
    for item in items:
        subtotal_item = item["quantity"] * item["unit_price"]
        rows += f"""
        <tr>
          <td style="padding:8px 12px;border-bottom:1px solid #eee;">{item['name']}</td>
          <td style="padding:8px 12px;border-bottom:1px solid #eee;text-align:center;">{item['quantity']}</td>
          <td style="padding:8px 12px;border-bottom:1px solid #eee;text-align:right;">${subtotal_item:,.2f}</td>
        </tr>
        """
    payment_labels = {
        "MERCADOPAGO": "MercadoPago", "BANK_TRANSFER": "Transferencia Bancaria",
        "PAYPAL": "PayPal", "CREDIT": "Tarjeta de Crédito",
        "DEBIT": "Tarjeta de Débito", "CARD": "Tarjeta", "CASH": "Efectivo",
    }
    payment_label = payment_labels.get(payment_method.upper(), payment_method)

    html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="color-scheme" content="light">
      <meta name="supported-color-schemes" content="light">
      <style>
        :root {{ color-scheme: light; }}
        body {{ font-family: Arial, sans-serif; background:#f4f4f4; margin:0; padding:0; }}
        .container {{ max-width:600px; margin:30px auto; background:#fff; border-radius:12px;
                      overflow:hidden; box-shadow:0 2px 12px rgba(0,0,0,0.08); }}
        .header {{ background: linear-gradient(to bottom,#79edd6,#a5efa2); padding:32px; text-align:center; }}
        .header h1 {{ margin:0; font-size:28px; color:#010101 !important; }}
        .header p {{ margin:6px 0 0; font-size:14px; color:#010101 !important; }}
        .body {{ padding:28px 32px; }}
        .info-box {{ background:#fefce8; border:1px solid #fde68a; border-radius:8px;
                     padding:16px 20px; margin-bottom:24px; }}
        .info-box p {{ margin:4px 0; font-size:14px; color:#92400e; }}
        .refund-box {{ background:#f0fdf4; border:1px solid #bbf7d0; border-radius:8px;
                       padding:14px 20px; margin-bottom:20px; font-size:14px; color:#166534; }}
        table {{ width:100%; border-collapse:collapse; margin-bottom:20px; font-size:14px; }}
        thead tr {{ background:#f3f4f6; }}
        thead th {{ padding:10px 12px; text-align:left; color:#555; font-weight:600; }}
        .totals {{ text-align:right; font-size:14px; }}
        .totals td {{ padding:4px 12px; }}
        .total-row td {{ font-size:17px; font-weight:bold; color:#b45309; padding-top:12px; }}
        .footer {{ background: linear-gradient(to bottom,#a5efa2,#79edd6); color:#010101 !important;
                   text-align:center; padding:20px; font-size:12px; }}
      </style>
    </head>
    <body>
      <div class="container">
        <div class="header">
          <h1 style="color:#010101;">Beat<span style="color:#328c2f;">Hub</span><span style="color:#010101;">.ar</span></h1>
          <p>❌ Pedido cancelado</p>
        </div>
        <div class="body">
          <p style="font-size:16px;">¡Hola, <strong>{client_name}</strong>!</p>
          <p style="color:#555;font-size:14px;margin-top:0;">
            Tu pedido <strong>#{order_id}</strong> fue <strong style="color:#b45309;">cancelado</strong> exitosamente.
          </p>

          <div class="refund-box">
            ✅ <strong>Tu dinero será reintegrado</strong> según los tiempos habituales del método de pago utilizado (<strong>{payment_label}</strong>).
          </div>

          <div class="info-box">
            <p><strong>Número de Orden:</strong> #{order_id}</p>
            <p><strong>Factura:</strong> {bill_number}</p>
            <p><strong>Método de Pago:</strong> {payment_label}</p>
          </div>

          <p style="font-size:13px;font-weight:600;color:#555;margin-bottom:8px;">Productos cancelados:</p>
          <table>
            <thead>
              <tr>
                <th>Producto</th>
                <th style="text-align:center;">Cant.</th>
                <th style="text-align:right;">Subtotal</th>
              </tr>
            </thead>
            <tbody>{rows}</tbody>
          </table>

          <table class="totals">
            <tr><td style="color:#555;">Subtotal (sin IVA):</td><td><strong>${subtotal:,.2f}</strong></td></tr>
            <tr><td style="color:#555;">IVA (21%):</td><td><strong>${iva:,.2f}</strong></td></tr>
            <tr class="total-row"><td>Total a reintegrar:</td><td>${total:,.2f}</td></tr>
          </table>

          <p style="font-size:13px;color:#888;margin-top:8px;">
            Si tenés alguna consulta sobre tu reintegro no dudes en contactarnos.
          </p>
        </div>
        <div class="footer">
          <p>BeatHub.ar · Mendoza, Argentina</p>
          <p>Contactanos al +549&nbsp;(3772)&nbsp;584894</p>
        </div>
      </div>
    </body>
    </html>
    """
    try:
        conf = get_mail_config()
        fm = FastMail(conf)
        message = MessageSchema(
            subject=f"BeatHub.ar — Tu pedido #{order_id} fue cancelado",
            recipients=[to_email],
            body=html,
            subtype=MessageType.html,
        )
        await fm.send_message(message)
    except Exception as e:
        print(f"[EMAIL ERROR] No se pudo enviar email de cancelación a {to_email}: {e}")


async def send_order_in_progress_email(
    to_email: str,
    client_name: str,
    order_id: int,
    bill_number: str,
    items: list,
    subtotal: float,
    iva: float,
    total: float,
    payment_method: str,
):
    """Notify user that their order is now in transit."""
    rows = ""
    for item in items:
        subtotal_item = item["quantity"] * item["unit_price"]
        rows += f"""
        <tr>
          <td style="padding:8px 12px;border-bottom:1px solid #eee;">{item['name']}</td>
          <td style="padding:8px 12px;border-bottom:1px solid #eee;text-align:center;">{item['quantity']}</td>
          <td style="padding:8px 12px;border-bottom:1px solid #eee;text-align:right;">${subtotal_item:,.2f}</td>
        </tr>
        """
    payment_labels = {
        "MERCADOPAGO": "MercadoPago", "BANK_TRANSFER": "Transferencia Bancaria",
        "PAYPAL": "PayPal", "CREDIT": "Tarjeta de Crédito",
        "DEBIT": "Tarjeta de Débito", "CARD": "Tarjeta", "CASH": "Efectivo",
    }
    payment_label = payment_labels.get(payment_method.upper(), payment_method)

    html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="color-scheme" content="light">
      <meta name="supported-color-schemes" content="light">
      <style>
        :root {{ color-scheme: light; }}
        body {{ font-family: Arial, sans-serif; background:#f4f4f4; margin:0; padding:0; }}
        .container {{ max-width:600px; margin:30px auto; background:#fff; border-radius:12px;
                      overflow:hidden; box-shadow:0 2px 12px rgba(0,0,0,0.08); }}
        .header {{ background: linear-gradient(to bottom,#79edd6,#a5efa2); padding:32px; text-align:center; }}
        .header h1 {{ margin:0; font-size:28px; color:#010101 !important; }}
        .header p {{ margin:6px 0 0; font-size:14px; color:#010101 !important; }}
        .body {{ padding:28px 32px; }}
        .info-box {{ background:#eff6ff; border:1px solid #bfdbfe; border-radius:8px;
                     padding:16px 20px; margin-bottom:24px; }}
        .info-box p {{ margin:4px 0; font-size:14px; color:#1e40af; }}
        table {{ width:100%; border-collapse:collapse; margin-bottom:20px; font-size:14px; }}
        thead tr {{ background:#f3f4f6; }}
        thead th {{ padding:10px 12px; text-align:left; color:#555; font-weight:600; }}
        .totals {{ text-align:right; font-size:14px; }}
        .totals td {{ padding:4px 12px; }}
        .total-row td {{ font-size:17px; font-weight:bold; color:#1d4ed8; padding-top:12px; }}
        .footer {{ background: linear-gradient(to bottom,#a5efa2,#79edd6); color:#010101 !important;
                   text-align:center; padding:20px; font-size:12px; }}
      </style>
    </head>
    <body>
      <div class="container">
        <div class="header">
          <h1 style="color:#010101;">Beat<span style="color:#328c2f;">Hub</span><span style="color:#010101;">.ar</span></h1>
          <p>🚚 ¡Tu pedido está en camino!</p>
        </div>
        <div class="body">
          <p style="font-size:16px;">¡Hola, <strong>{client_name}</strong>! 📬</p>
          <p style="color:#555;font-size:14px;margin-top:0;">
            Buenas noticias: tu pedido ya fue <strong style="color:#1d4ed8;">despachado</strong> y está en camino a tu domicilio.
          </p>

          <div class="info-box">
            <p><strong>Número de Orden:</strong> #{order_id}</p>
            <p><strong>Factura:</strong> {bill_number}</p>
            <p><strong>Método de Pago:</strong> {payment_label}</p>
          </div>

          <table>
            <thead>
              <tr>
                <th>Producto</th>
                <th style="text-align:center;">Cant.</th>
                <th style="text-align:right;">Subtotal</th>
              </tr>
            </thead>
            <tbody>{rows}</tbody>
          </table>

          <table class="totals">
            <tr><td style="color:#555;">Subtotal (sin IVA):</td><td><strong>${subtotal:,.2f}</strong></td></tr>
            <tr><td style="color:#555;">IVA (21%):</td><td><strong>${iva:,.2f}</strong></td></tr>
            <tr class="total-row"><td>Total:</td><td>${total:,.2f}</td></tr>
          </table>

          <p style="font-size:13px;color:#888;margin-top:16px;">
            Podés ver el estado actualizado en la sección <strong>Seguimiento</strong> de nuestra web.
          </p>
        </div>
        <div class="footer">
          <p>BeatHub.ar · Mendoza, Argentina</p>
          <p>Si tenés alguna consulta, contactanos al +549&nbsp;(3772)&nbsp;584894</p>
        </div>
      </div>
    </body>
    </html>
    """
    try:
        conf = get_mail_config()
        fm = FastMail(conf)
        message = MessageSchema(
            subject=f"BeatHub.ar — 🚚 Tu pedido #{order_id} está en camino",
            recipients=[to_email],
            body=html,
            subtype=MessageType.html,
        )
        await fm.send_message(message)
    except Exception as e:
        print(f"[EMAIL ERROR] No se pudo enviar email de en camino a {to_email}: {e}")


async def send_order_delivered_email(
    to_email: str,
    client_name: str,
    order_id: int,
    bill_number: str,
    items: list,
    subtotal: float,
    iva: float,
    total: float,
    payment_method: str,
):
    """Notify user that their order has been delivered."""
    rows = ""
    for item in items:
        subtotal_item = item["quantity"] * item["unit_price"]
        rows += f"""
        <tr>
          <td style="padding:8px 12px;border-bottom:1px solid #eee;">{item['name']}</td>
          <td style="padding:8px 12px;border-bottom:1px solid #eee;text-align:center;">{item['quantity']}</td>
          <td style="padding:8px 12px;border-bottom:1px solid #eee;text-align:right;">${subtotal_item:,.2f}</td>
        </tr>
        """
    payment_labels = {
        "MERCADOPAGO": "MercadoPago", "BANK_TRANSFER": "Transferencia Bancaria",
        "PAYPAL": "PayPal", "CREDIT": "Tarjeta de Crédito",
        "DEBIT": "Tarjeta de Débito", "CARD": "Tarjeta", "CASH": "Efectivo",
    }
    payment_label = payment_labels.get(payment_method.upper(), payment_method)

    html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="color-scheme" content="light">
      <meta name="supported-color-schemes" content="light">
      <style>
        :root {{ color-scheme: light; }}
        body {{ font-family: Arial, sans-serif; background:#f4f4f4; margin:0; padding:0; }}
        .container {{ max-width:600px; margin:30px auto; background:#fff; border-radius:12px;
                      overflow:hidden; box-shadow:0 2px 12px rgba(0,0,0,0.08); }}
        .header {{ background: linear-gradient(to bottom,#79edd6,#a5efa2); padding:32px; text-align:center; }}
        .header h1 {{ margin:0; font-size:28px; color:#010101 !important; }}
        .header p {{ margin:6px 0 0; font-size:14px; color:#010101 !important; }}
        .body {{ padding:28px 32px; }}
        .info-box {{ background:#f0fdf4; border:1px solid #bbf7d0; border-radius:8px;
                     padding:16px 20px; margin-bottom:24px; }}
        .info-box p {{ margin:4px 0; font-size:14px; color:#166534; }}
        table {{ width:100%; border-collapse:collapse; margin-bottom:20px; font-size:14px; }}
        thead tr {{ background:#f3f4f6; }}
        thead th {{ padding:10px 12px; text-align:left; color:#555; font-weight:600; }}
        .totals {{ text-align:right; font-size:14px; }}
        .totals td {{ padding:4px 12px; }}
        .total-row td {{ font-size:17px; font-weight:bold; color:#166534; padding-top:12px; }}
        .footer {{ background: linear-gradient(to bottom,#a5efa2,#79edd6); color:#010101 !important;
                   text-align:center; padding:20px; font-size:12px; }}
      </style>
    </head>
    <body>
      <div class="container">
        <div class="header">
          <h1 style="color:#010101;">Beat<span style="color:#328c2f;">Hub</span><span style="color:#010101;">.ar</span></h1>
          <p>📦 ¡Tu pedido fue entregado!</p>
        </div>
        <div class="body">
          <p style="font-size:16px;">¡Hola, <strong>{client_name}</strong>! 🎉</p>
          <p style="color:#555;font-size:14px;margin-top:0;">
            Tu pedido fue <strong style="color:#166534;">entregado exitosamente</strong>. ¡Esperamos que disfrutes tu compra!
          </p>
          <p style="color:#888;font-size:13px;margin-top:-8px;">
            Si tenés algún inconveniente con el producto podés solicitar una devolución desde la sección <strong>Mis Compras</strong>.
          </p>

          <div class="info-box">
            <p><strong>Número de Orden:</strong> #{order_id}</p>
            <p><strong>Factura:</strong> {bill_number}</p>
            <p><strong>Método de Pago:</strong> {payment_label}</p>
          </div>

          <table>
            <thead>
              <tr>
                <th>Producto</th>
                <th style="text-align:center;">Cant.</th>
                <th style="text-align:right;">Subtotal</th>
              </tr>
            </thead>
            <tbody>{rows}</tbody>
          </table>

          <table class="totals">
            <tr><td style="color:#555;">Subtotal (sin IVA):</td><td><strong>${subtotal:,.2f}</strong></td></tr>
            <tr><td style="color:#555;">IVA (21%):</td><td><strong>${iva:,.2f}</strong></td></tr>
            <tr class="total-row"><td>Total:</td><td>${total:,.2f}</td></tr>
          </table>
        </div>
        <div class="footer">
          <p>BeatHub.ar · Mendoza, Argentina</p>
          <p>¡Gracias por tu compra! Si tenés alguna consulta, contactanos al +549&nbsp;(3772)&nbsp;584894</p>
        </div>
      </div>
    </body>
    </html>
    """
    try:
        conf = get_mail_config()
        fm = FastMail(conf)
        message = MessageSchema(
            subject=f"BeatHub.ar — 📦 ¡Tu pedido #{order_id} fue entregado!",
            recipients=[to_email],
            body=html,
            subtype=MessageType.html,
        )
        await fm.send_message(message)
    except Exception as e:
        print(f"[EMAIL ERROR] No se pudo enviar email de entregado a {to_email}: {e}")


async def send_password_reset_email(to_email: str, client_name: str, token: str):
    """Send a password reset email with a signed link."""
    import os
    frontend_url = os.getenv("FRONTEND_URL", "http://localhost:5173")
    reset_link = f"{frontend_url}/reset-password?token={token}"

    html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head><meta charset="UTF-8"><meta name="color-scheme" content="light"><meta name="supported-color-schemes" content="light"><style>:root{{color-scheme:light}}</style></head>
    <body style="margin:0;padding:0;background:#f3f4f6;font-family:Arial,sans-serif">
      <div style="max-width:560px;margin:40px auto;background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,.1)">
        <div style="background:linear-gradient(to bottom,#79edd6,#a5efa2);padding:32px;text-align:center">
          <h1 style="margin:0;color:#010101 !important;font-size:26px">Beat<span style="color:#328c2f !important;">Hub</span><span style="color:#010101 !important;">.ar</span></h1>
          <p style="margin:8px 0 0;color:#010101 !important;font-size:14px">Recuperación de contraseña</p>
        </div>
        <div style="padding:32px">
          <p style="color:#374151;font-size:16px">Hola <strong>{client_name}</strong>,</p>
          <p style="color:#6b7280">Recibimos una solicitud para restablecer la contraseña de tu cuenta. Hacé clic en el botón de abajo para crear una nueva.</p>
          <div style="text-align:center;margin:32px 0">
            <a href="{reset_link}" style="background:linear-gradient(135deg,#4d1869,#5f247e);color:#fff;padding:14px 32px;border-radius:8px;text-decoration:none;font-weight:bold;font-size:15px">Restablecer contraseña</a>
          </div>
          <p style="color:#9ca3af;font-size:13px">Este enlace expira en <strong>1 hora</strong>. Si no solicitaste esto, podés ignorar este correo.</p>
          <p style="color:#9ca3af;font-size:12px;word-break:break-all">O copiá este link: {reset_link}</p>
        </div>
        <div style="background:linear-gradient(to bottom,#a5efa2,#79edd6);padding:16px;text-align:center;color:#010101 !important;font-size:12px">
          <p>BeatHub.ar · Mendoza, Argentina</p>
        </div>
      </div>
    </body>
    </html>
    """

    try:
        conf = get_mail_config()
        fm = FastMail(conf)
        message = MessageSchema(
            subject="BeatHub.ar — Restablecer contraseña",
            recipients=[to_email],
            body=html,
            subtype=MessageType.html,
        )
        await fm.send_message(message)
    except Exception as e:
        print(f"[EMAIL ERROR] No se pudo enviar reset a {to_email}: {e}")


async def send_welcome_email(to_email: str, client_name: str):
    """Send a welcome email when a new client registers."""
    html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head><meta charset="UTF-8"><meta name="color-scheme" content="light"><meta name="supported-color-schemes" content="light"><style>:root{{color-scheme:light}}</style></head>
    <body style="margin:0;padding:0;background:#f3f4f6;font-family:Arial,sans-serif">
      <div style="max-width:560px;margin:40px auto;background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,.1)">
        <div style="background:linear-gradient(to bottom,#79edd6,#a5efa2);padding:32px;text-align:center">
          <h1 style="margin:0;color:#010101 !important;font-size:28px">Beat<span style="color:#328c2f !important;">Hub</span><span style="color:#010101 !important;">.ar</span></h1>
          <p style="margin:10px 0 0;color:#010101 !important;font-size:14px">Bienvenido/a a la comunidad</p>
        </div>
        <div style="padding:36px">
          <p style="color:#374151;font-size:17px;margin-bottom:8px">Hola <strong>{client_name}</strong> 🎉</p>
          <p style="color:#6b7280;line-height:1.6">
            Gracias por registrarte en <strong>BeatHub.ar</strong>. Ya podés explorar nuestro catálogo, agregar productos al carrito y realizar tus compras de forma segura.
          </p>
          <div style="background:#f9fafb;border-radius:10px;padding:20px;margin:24px 0;border-left:4px solid #5f247e">
            <p style="margin:0;color:#374151;font-size:14px"><strong>📦 Realizá tus compras</strong> y recibirás la factura al instante por email.</p>
            <p style="margin:10px 0 0;color:#374151;font-size:14px"><strong>📍 Seguimiento</strong> en tiempo real desde tu cuenta.</p>
            <p style="margin:10px 0 0;color:#374151;font-size:14px"><strong>🔒 Tu información</strong> siempre protegida.</p>
          </div>
          <p style="color:#6b7280;font-size:14px">
            Si no fuiste vos quien se registró, podés ignorar este correo.
          </p>
        </div>
        <div style="background:linear-gradient(to bottom,#a5efa2,#79edd6);padding:20px;text-align:center;color:#010101 !important;font-size:12px">
          <p style="margin:0">BeatHub.ar &middot; Mendoza, Argentina</p>
          <p style="margin:6px 0 0">Este es un correo automático, por favor no respondas.</p>
        </div>
      </div>
    </body>
    </html>
    """

    try:
        conf = get_mail_config()
        fm = FastMail(conf)
        message = MessageSchema(
            subject="BeatHub.ar — ¡Bienvenido/a!",
            recipients=[to_email],
            body=html,
            subtype=MessageType.html,
        )
        await fm.send_message(message)
    except Exception as e:
        print(f"[EMAIL ERROR] No se pudo enviar bienvenida a {to_email}: {e}")


async def send_return_requested_email(
    to_email: str,
    client_name: str,
    order_id: int,
    bill_number: str,
):
    """Notify user that their return request was received and they must contact customer service."""
    html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head><meta charset="UTF-8"/></head>
    <body style="margin:0;padding:0;background:#f4f4f5;font-family:'Segoe UI',Arial,sans-serif;">
    <table width="100%" cellpadding="0" cellspacing="0" style="background:#f4f4f5;padding:40px 0;">
      <tr><td align="center">
        <table width="600" cellpadding="0" cellspacing="0" style="background:#ffffff;border-radius:16px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,0.08);">
          <!-- Header -->
          <tr>
            <td style="background:linear-gradient(135deg,#f97316,#fb923c);padding:36px 40px;text-align:center;">
              <h1 style="margin:0;color:#fff;font-size:28px;font-weight:800;letter-spacing:-0.5px;">↩️ Devolución solicitada</h1>
              <p style="margin:8px 0 0;color:rgba(255,255,255,0.85);font-size:15px;">BeatHub.ar</p>
            </td>
          </tr>
          <!-- Body -->
          <tr>
            <td style="padding:36px 40px;">
              <p style="font-size:16px;color:#374151;margin:0 0 16px;">Hola, <strong>{client_name}</strong> 👋</p>
              <p style="font-size:15px;color:#6b7280;margin:0 0 24px;">
                Recibimos tu solicitud de devolución para el pedido <strong>#{order_id}</strong> (Factura: <code style="background:#f3f4f6;padding:2px 6px;border-radius:4px;">{bill_number}</code>). Ya estamos al tanto y nos pondremos en contacto con vos a la brevedad.
              </p>

              <!-- Info box -->
              <div style="background:#fff7ed;border-left:4px solid #f97316;border-radius:8px;padding:18px 20px;margin-bottom:24px;">
                <p style="margin:0 0 8px;font-weight:700;color:#c2410c;font-size:14px;">⚠️ Importante</p>
                <p style="margin:0;color:#9a3412;font-size:14px;line-height:1.6;">
                  <strong>No respondas este correo directamente.</strong> Para gestionar tu devolución, contactate con nuestro servicio al cliente a través de los canales oficiales de BeatHub.ar. Tené a mano el número de pedido y la factura al momento de comunicarte.
                </p>
              </div>

              <!-- Steps -->
              <p style="font-size:14px;font-weight:700;color:#374151;margin:0 0 12px;">¿Qué pasa ahora?</p>
              <ol style="padding-left:20px;color:#6b7280;font-size:14px;line-height:2;">
                <li>Un agente de BeatHub.ar revisará tu solicitud</li>
                <li>Te contactaremos para coordinar la logística de devolución</li>
                <li>Una vez recibido el producto, procesaremos el reintegro</li>
              </ol>

              <p style="font-size:13px;color:#9ca3af;margin:28px 0 0;">Si tenés alguna urgencia, buscanos en nuestros canales oficiales. Gracias por tu paciencia.</p>
            </td>
          </tr>
          <!-- Footer -->
          <tr>
            <td style="background:#f9fafb;padding:20px 40px;text-align:center;border-top:1px solid #e5e7eb;">
              <p style="margin:0;font-size:12px;color:#9ca3af;">© 2026 BeatHub.ar · Todos los derechos reservados</p>
            </td>
          </tr>
        </table>
      </td></tr>
    </table>
    </body>
    </html>
    """
    try:
        conf = get_mail_config()
        fm = FastMail(conf)
        message = MessageSchema(
            subject=f"BeatHub.ar — Devolución solicitada para tu pedido #{order_id}",
            recipients=[to_email],
            body=html,
            subtype=MessageType.html,
        )
        await fm.send_message(message)
    except Exception as e:
        print(f"[EMAIL ERROR] No se pudo enviar email de devolución a {to_email}: {e}")


async def send_return_contact_email(
    to_email: str,
    client_name: str,
    order_id: int,
    bill_number: str,
):
    """Admin initiates contact with user to coordinate product return logistics."""
    html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head><meta charset="UTF-8"/></head>
    <body style="margin:0;padding:0;background:#f4f4f5;font-family:'Segoe UI',Arial,sans-serif;">
    <table width="100%" cellpadding="0" cellspacing="0" style="background:#f4f4f5;padding:40px 0;">
      <tr><td align="center">
        <table width="600" cellpadding="0" cellspacing="0" style="background:#ffffff;border-radius:16px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,0.08);">
          <!-- Header -->
          <tr>
            <td style="background:linear-gradient(135deg,#7c3aed,#9333ea);padding:36px 40px;text-align:center;">
              <h1 style="margin:0;color:#fff;font-size:28px;font-weight:800;letter-spacing:-0.5px;">📋 Gestión de devolución</h1>
              <p style="margin:8px 0 0;color:rgba(255,255,255,0.85);font-size:15px;">BeatHub.ar — Servicio al Cliente</p>
            </td>
          </tr>
          <!-- Body -->
          <tr>
            <td style="padding:36px 40px;">
              <p style="font-size:16px;color:#374151;margin:0 0 16px;">Hola, <strong>{client_name}</strong> 👋</p>
              <p style="font-size:15px;color:#6b7280;margin:0 0 24px;">
                Nuestro equipo ya procesó tu solicitud de devolución del pedido <strong>#{order_id}</strong> (Factura: <code style="background:#f3f4f6;padding:2px 6px;border-radius:4px;">{bill_number}</code>). Para completar el proceso necesitamos que sigas los pasos a continuación.
              </p>

              <!-- Steps box -->
              <div style="background:#f5f3ff;border-left:4px solid #7c3aed;border-radius:8px;padding:18px 20px;margin-bottom:24px;">
                <p style="margin:0 0 12px;font-weight:700;color:#5b21b6;font-size:14px;">📦 Pasos para devolver tu producto</p>
                <ol style="padding-left:20px;color:#6d28d9;font-size:14px;line-height:2;margin:0;">
                  <li>Empaquetá el producto en su embalaje original (o similar)</li>
                  <li>Incluí una copia de la factura <strong>{bill_number}</strong> dentro del paquete</li>
                  <li>Acercá el paquete a la sucursal de paquetería más cercana</li>
                  <li>Enviá el número de seguimiento a nuestro servicio al cliente</li>
                </ol>
              </div>

              <!-- Warning -->
              <div style="background:#fefce8;border-left:4px solid #ca8a04;border-radius:8px;padding:16px 20px;margin-bottom:24px;">
                <p style="margin:0;color:#92400e;font-size:13px;">
                  ⚠️ <strong>No respondas este correo directamente.</strong> Usá los canales oficiales de BeatHub.ar para cualquier consulta adicional. Tené siempre a mano tu número de pedido <strong>#{order_id}</strong>.
                </p>
              </div>

              <p style="font-size:13px;color:#9ca3af;margin:0;">Una vez que recibamos el producto en nuestras instalaciones, procesaremos el reintegro según el método de pago original. El tiempo puede variar entre 3 y 10 días hábiles.</p>
            </td>
          </tr>
          <!-- Footer -->
          <tr>
            <td style="background:#f9fafb;padding:20px 40px;text-align:center;border-top:1px solid #e5e7eb;">
              <p style="margin:0;font-size:12px;color:#9ca3af;">© 2026 BeatHub.ar · Todos los derechos reservados</p>
            </td>
          </tr>
        </table>
      </td></tr>
    </table>
    </body>
    </html>
    """
    try:
        conf = get_mail_config()
        fm = FastMail(conf)
        message = MessageSchema(
            subject=f"BeatHub.ar — Instrucciones para devolver tu pedido #{order_id}",
            recipients=[to_email],
            body=html,
            subtype=MessageType.html,
        )
        await fm.send_message(message)
    except Exception as e:
        print(f"[EMAIL ERROR] No se pudo enviar email de contacto de devolución a {to_email}: {e}")
