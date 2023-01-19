from abc import ABC, abstractmethod
from datetime import timedelta

class ICrypto(ABC):

    @abstractmethod
    def generate_token(subject: str, expires_type: str, expire_duration: timedelta) -> str:
        pass

    @abstractmethod
    def verify_token(token: str, subject: str) -> str | None:
        pass