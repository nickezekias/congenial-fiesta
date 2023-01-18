from abc import ABC, abstractmethod
from datetime import timedelta
from typing import Any

from src.domain.account.user import User


class IAuthenticator(ABC):

    @abstractmethod
    def create_access_token(
        subject: str | Any, expires_delta: timedelta = None
    ) -> str:
        pass

    @abstractmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        pass

    @abstractmethod
    def get_password_hash(password: str) -> str:
        pass

    """ Get current user """
    @abstractmethod
    def user() -> User:
        pass
