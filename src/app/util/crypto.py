import logging
from datetime import datetime, timedelta
from jose import jwt
from src.domain.util.i_crypto import ICrypto

from src.app.config.app import settings;

class Crypto(ICrypto):
    EXPIRES_TYPE_SECONDS = "seconds"
    EXPIRES_TYPE_MINUTES = "minutes"
    EXPIRES_TYPE_HOURS = "hours"

    @staticmethod
    def generate_token(subject: str, expires_type: str, expires_duration: int) -> str:
        if expires_type == "hours":
            delta = timedelta(hours=expires_duration)
        elif expires_type == "minutes":
            delta = timedelta(minutes=expires_duration)
        else:
            delta = timedelta(seconds=expires_duration)
        now = datetime.utcnow()
        expires = now + delta
        exp = expires.timestamp()
        encoded_jwt = jwt.encode(
            {"exp": exp, "nbf": now, "sub": subject}, settings.APP_KEY, algorithm=settings.CRYPT_ALGORITHM,
        )
        return encoded_jwt

    @staticmethod
    def verify_token(token: str) -> str | None:
        try:
            decoded_token = jwt.decode(token, settings.APP_KEY, algorithms=[settings.CRYPT_ALGORITHM])
            return decoded_token["sub"]
        except jwt.JWTError:
            return None
