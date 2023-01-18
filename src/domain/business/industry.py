from dataclasses import dataclass

from src.domain.base.entity import Entity

@dataclass
class Industry(Entity):
    id: str
    name: str
    description: str