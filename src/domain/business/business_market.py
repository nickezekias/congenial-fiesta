from dataclasses import dataclass

from src.domain.base.entity import Entity

@dataclass
class BusinessMarket(Entity):
    id: str
    name: str
    description: str