import os
import sys
import json
import logging
from typing import Any
from pydantic import (
    AnyHttpUrl,
    BaseSettings
)
from loguru import logger

def _list_parse_fallback(v: Any) -> Any:
    try:
        return json.loads(v)
    except Exception:
        return v.split(",")

class LoggingSettings(BaseSettings):
    LOGGING_LEVEL: int = logging.INFO  # logging levels are ints

class Settings(BaseSettings):
    APP_NAME: str = os.getenv("APP_NAME", "c8gd2s-backend"),
    API_V1_STR: str = "/api/v1"
    APP_DEBUG: bool = os.getenv("APP_DEBUG", False)

    APP_KEY: str = os.getenv("APP_KEY", "randfi8398238xkl48x8")
    CRYPT_ALGORITHM: str = "HS256"

    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    #email
    EMAIL_TEMPLATES_DIR="src/app/email/templates"
    MAIL_VERIFY_TOKEN_EXPIRE_HOURS: int = 1
    MAIL_PASSWORD_RESET_TOKEN_EXPIRE_MINUTES: int = 60
    MAIL_USERNAME = os.getenv("MAIL_USERNAME", "")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD", "")
    MAIL_FROM_NAME = os.getenv("APP_NAME")
    MAIL_FROM_ADDRESS = os.getenv("MAIL_FROM_ADDRESS", "admin@noenv.com")
    MAIL_PORT = os.getenv("MAIL_PORT", "")
    MAIL_HOST = os.getenv("MAIL_HOST", "")

    # logging
    logging: LoggingSettings = LoggingSettings()

    DOMAIN: str = f"{os.getenv('APP_HOST', '0.0.0.0')}:{os.getenv('APP_PORT', '8000')}"
    # logger.debug(os.getenv("APP_URL", "http://localhost:8000"))
    SERVER_HOST: AnyHttpUrl = "http://localhost:8000"  # type: ignore

    # BACKEND_CORS_ORIGINS is a comma-separated list of origins
    # e.g: http://localhost,http://localhost:4200,http://localhost:3000
    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = [
        "http://localhost:8000",
        "https://localhost:8000",
        "http://localhost:8080",  # type: ignore
        "http://localhost:5173",  # type: ignore
        "https://localhost:8080",  # type: ignore
        "https://localhost:5173",  # type: ignore
    ]

    class Config:
        case_sensitive = True
        json_loads = _list_parse_fallback


def setup_app_logging(config: Settings) -> None:
    """Prepare custom logging for our application."""
    LOGGERS = ("uvicorn.asgi", "uvicorn.access")
    for logger_name in LOGGERS:
        logging_logger = logging.getLogger(logger_name)

    logger.configure(
        handlers=[{"sink": sys.stderr, "level": config.logging.LOGGING_LEVEL}]
    )

settings = Settings()