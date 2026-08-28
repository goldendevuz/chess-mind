from datetime import datetime, timedelta, timezone

from jose import jwt

from .config import settings


def create_access_token(subject: str, minutes: int = 15) -> str:
    payload = {
        "sub": subject,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=minutes),
        "typ": "access",
    }
    return jwt.encode(payload, settings.jwt_secret, algorithm="HS256")

