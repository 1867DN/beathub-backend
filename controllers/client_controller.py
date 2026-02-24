"""Client controller with proper dependency injection."""
from fastapi import Depends, Header, HTTPException, status
from sqlalchemy.orm import Session

from controllers.base_controller_impl import BaseControllerImpl
from schemas.client_schema import ClientSchema
from services.client_service import ClientService
from services.auth_service import hash_password, decode_token
from services.email_service import send_welcome_email
from config.database import get_db
from models.client import ClientModel


class ClientController(BaseControllerImpl):
    """Controller for Client entity — overrides create to hash password."""

    def __init__(self):
        super().__init__(
            schema=ClientSchema,
            service_factory=lambda db: ClientService(db),
            tags=["Clients"]
        )
        self._register_client_routes()

    def _register_client_routes(self):
        """Override POST / to hash password and set default role before saving."""

        @self.router.post("/register/", response_model=ClientSchema, status_code=status.HTTP_201_CREATED)
        async def register_client(
            schema_in: ClientSchema,
            db: Session = Depends(get_db)
        ):
            """Register a new client — always role=user, password hashed."""
            data = schema_in.model_dump(exclude_unset=True)
            # Hash password if provided
            raw_password = data.pop("password", None)
            data.pop("password_hash", None)
            data["role"] = "user"  # always user on self-register
            if raw_password:
                data["password_hash"] = hash_password(raw_password)
            else:
                data["password_hash"] = ""
            client = ClientModel(**data)
            db.add(client)
            db.commit()
            db.refresh(client)
            # Send welcome email (non-blocking)
            try:
                await send_welcome_email(client.email, client.name)
            except Exception as e:
                print(f"[EMAIL] Welcome email failed: {e}")
            return client

        @self.router.get("/admin-all/", status_code=status.HTTP_200_OK)
        async def admin_all_clients(
            authorization: str = Header(None),
            db: Session = Depends(get_db)
        ):
            """Admin only: return all registered users."""
            if not authorization or not authorization.startswith("Bearer "):
                raise HTTPException(status_code=401, detail="No autenticado")
            payload = decode_token(authorization[7:])
            if not payload or payload.get("role") != "admin":
                raise HTTPException(status_code=403, detail="Acceso denegado")
            clients = db.query(ClientModel).order_by(ClientModel.id_key.desc()).all()
            return [
                {
                    "id": c.id_key,
                    "name": c.name,
                    "lastname": c.lastname,
                    "email": c.email,
                    "telephone": c.telephone,
                    "role": c.role,
                }
                for c in clients
            ]

        @self.router.patch("/{client_id}/role/", status_code=status.HTTP_200_OK)
        async def update_client_role(
            client_id: int,
            authorization: str = Header(None),
            db: Session = Depends(get_db)
        ):
            """Admin only: toggle user role between user and admin."""
            if not authorization or not authorization.startswith("Bearer "):
                raise HTTPException(status_code=401, detail="No autenticado")
            payload = decode_token(authorization[7:])
            if not payload or payload.get("role") != "admin":
                raise HTTPException(status_code=403, detail="Acceso denegado")
            client = db.query(ClientModel).filter(ClientModel.id_key == client_id).first()
            if not client:
                raise HTTPException(status_code=404, detail="Usuario no encontrado")
            client.role = "admin" if client.role == "user" else "user"
            db.commit()
            db.refresh(client)
            return {"id": client.id_key, "role": client.role}
