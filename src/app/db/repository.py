from typing import Generic, TypeVar
from src.domain.base.i_repository import IRepository
from src.domain.base.mapper import Mapper
from src.app.db.models.user_orm import UserORM
from src.app.db.base_class import Base as BaseORM

TEntity = TypeVar('TEntity')
ORMEntity = TypeVar('ORMEntity')
DbContext = TypeVar('DbContext')
TQuery = TypeVar('TQuery')

class Repository(Generic[ORMEntity, TEntity], IRepository[ORMEntity, TEntity]):
    db: DbContext
    mapper: Mapper

    def __init__(self, db: DbContext, mapper: Mapper) -> None:
        self.db = db
        self.mapper = mapper

    def get(self, id: int | str) -> TEntity:
        pass

    def getAll(self) -> list[TEntity]:
        orms: list[ORMEntity] = self.db.query.all()
        entities = self.mapper.mapToDomainList(orms)
        return entities

    def find(self, query: TQuery) -> list[TEntity]:
        orms: list[ORMEntity] = self.db.query.filter(query).all()
        entities = self.mapper.mapToDomainList(orms)
        return entities

    def add(self, entity: TEntity) -> TEntity:
        orm = self.mapper.mapFromDomain(entity)
        self.db.add(orm)
        user = self.mapper.mapToDomain(orm)
        return user

    def update(self, entity: TEntity) -> TEntity:
        pass



    #TODO: Return refreshed entities instead of input entities
    def add_range(self, entities: list[TEntity]) -> list[TEntity]:
        orms: list[ORMEntity] = self.mapper.mapFromDomainList(entities)
        self.db.add_all(orms)
        return entities

    def remove(self, entity: TEntity) -> None:
        orm = self.mapper.mapFromDomain(entity)
        self.db.remove(orm)

    def remove_range(self, entities: list[TEntity]) -> None:
        return super().remove_range()

    def commit(self) -> None:
        self.db.commit()

    def refresh(self, entity: TEntity) -> None:
        self.db.refresh(entity)





    
