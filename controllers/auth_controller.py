"""Auth controller: login, me, logout endpoints."""
from fastapi import APIRouter, Depends, HTTPException, status, Header
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session

from config.database import get_db
from services.auth_service import login_user, decode_token, create_reset_token, decode_reset_token, hash_password
from services.email_service import send_password_reset_email
from models.client import ClientModel

router = APIRouter(tags=["Auth"])


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


@router.post("/login/")
async def auth_login(req: LoginRequest, db: Session = Depends(get_db)):
    """Authenticate and return token + user data."""
    result = login_user(req.email, req.password, db)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas"
        )
    return result


@router.get("/me/")
async def auth_me(authorization: str = Header(None), db: Session = Depends(get_db)):
    """Return the authenticated user's profile."""
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="No autenticado")
    token = authorization[7:]
    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido o expirado")
    client = db.query(ClientModel).filter(ClientModel.id_key == payload["id"]).first()
    if not client:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return {
        "id_key": client.id_key,
        "name": client.name,
        "lastname": client.lastname,
        "email": client.email,
        "role": client.role or "user",
    }


@router.post("/logout/")
async def auth_logout():
    """Logout (client-side token removal)."""
    return {"message": "Sesión cerrada exitosamente"}


class ForgotPasswordRequest(BaseModel):
    email: EmailStr


class ResetPasswordRequest(BaseModel):
    token: str
    new_password: str


@router.post("/forgot-password/")
async def auth_forgot_password(req: ForgotPasswordRequest, db: Session = Depends(get_db)):
    """Send a password reset email if the email exists."""
    client = db.query(ClientModel).filter(ClientModel.email == req.email).first()
    # Always return 200 to avoid revealing whether email exists
    if client:
        token = create_reset_token(client.id_key, client.email)
        await send_password_reset_email(client.email, client.name, token)
    return {"message": "Si el correo está registrado, recibirás un email con instrucciones."}


@router.post("/reset-password/")
async def auth_reset_password(req: ResetPasswordRequest, db: Session = Depends(get_db)):
    """Reset a user's password using a valid reset token."""
    payload = decode_reset_token(req.token)
    if not payload:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El enlace es inválido o ya expiró.")
    client = db.query(ClientModel).filter(ClientModel.id_key == payload["id"]).first()
    if not client:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado.")
    client.password_hash = hash_password(req.new_password)
    db.commit()
    return {"message": "Contraseña actualizada correctamente."}
