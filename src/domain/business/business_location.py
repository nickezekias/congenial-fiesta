from dataclasses import dataclass

from src.domain.base.entity import Entity

@dataclass
class BusinessLocation(Entity):
    id: str
    name: str
    description: str