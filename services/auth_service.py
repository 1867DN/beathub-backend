"""Auth service: password hashing and token management (no external packages)."""
import hashlib
import hmac
import base64
import json
import time
import os

from sqlalchemy.orm import Session
from models.client import ClientModel

SECRET_KEY = os.getenv("SECRET_KEY", "beathub-secret-key-2025-leandro")


def hash_password(password: str) -> str:
    """Hash a password with a random salt using SHA-256."""
    salt = os.urandom(16).hex()
    h = hashlib.sha256((salt + password).encode()).hexdigest()
    return f"{salt}:{h}"


def verify_password(password: str, hashed: str) -> bool:
    """Verify a plaintext password against a stored hash."""
    if not hashed or ':' not in hashed:
        return False
    salt, h = hashed.split(":", 1)
    candidate = hashlib.sha256((salt + password).encode()).hexdigest()
    return hmac.compare_digest(candidate, h)


def create_token(user_id: int, role: str, email: str) -> str:
    """Create a signed token with 30-day expiry."""
    payload = {
        "id": user_id,
        "role": role,
        "email": email,
        "exp": int(time.time()) + 86400 * 30
    }
    payload_b64 = base64.b64encode(json.dumps(payload).encode()).decode()
    sig = hmac.new(SECRET_KEY.encode(), payload_b64.encode(), hashlib.sha256).hexdigest()
    return f"{payload_b64}.{sig}"


def decode_token(token: str) -> dict | None:
    """Decode and verify a token. Returns payload dict or None if invalid."""
    try:
        payload_b64, sig = token.rsplit(".", 1)
        expected_sig = hmac.new(SECRET_KEY.encode(), payload_b64.encode(), hashlib.sha256).hexdigest()
        if not hmac.compare_digest(sig, expected_sig):
            return None
        payload = json.loads(base64.b64decode(payload_b64).decode())
        if payload.get("exp", 0) < int(time.time()):
            return None
        return payload
    except Exception:
        return None


def create_reset_token(user_id: int, email: str) -> str:
    """Create a signed password-reset token valid for 1 hour."""
    payload = {"id": user_id, "email": email, "type": "reset", "exp": int(time.time()) + 3600}
    payload_b64 = base64.b64encode(json.dumps(payload).encode()).decode()
    sig = hmac.new(SECRET_KEY.encode(), payload_b64.encode(), hashlib.sha256).hexdigest()
    return f"{payload_b64}.{sig}"


def decode_reset_token(token: str) -> dict | None:
    """Decode and verify a reset token. Returns payload or None if invalid/expired."""
    try:
        payload_b64, sig = token.rsplit(".", 1)
        expected_sig = hmac.new(SECRET_KEY.encode(), payload_b64.encode(), hashlib.sha256).hexdigest()
        if not hmac.compare_digest(sig, expected_sig):
            return None
        payload = json.loads(base64.b64decode(payload_b64).decode())
        if payload.get("type") != "reset":
            return None
        if payload.get("exp", 0) < int(time.time()):
            return None
        return payload
    except Exception:
        return None


def login_user(email: str, password: str, db: Session) -> dict | None:
    """Authenticate user by email+password. Returns token+user dict or None."""
    client = db.query(ClientModel).filter(ClientModel.email == email).first()
    if not client:
        return None
    if not verify_password(password, client.password_hash or ""):
        return None
    role = client.role or "user"
    token = create_token(client.id_key, role, client.email)
    return {
        "token": token,
        "user": {
            "id_key": client.id_key,
            "name": client.name,
            "lastname": client.lastname,
            "email": client.email,
            "role": role,
        }
    }
