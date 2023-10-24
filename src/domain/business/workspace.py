from dataclasses import dataclass
from datetime import datetime
from typing import TypeVar

from src.domain.base.entity import Entity

Currency = TypeVar("Currency")

@dataclass
class Workspace(Entity):
    currency: Currency
    timezone: str
    # time_format: str
    # date_format: str
    id: str

    def __init__(
        self,
        id: str,
        currency: Currency,
        timezone: str,
        # time_format: str,
        # date_format: str
    ) -> None:
        self.id = id
        self.currency = currency
        self.timezone = timezone
        # self.time_format = time_format
        # self.date_format = date_format
        super().__init__()
