from src.domain.base.mapper import Mapper
from src.domain.business.business import Business
from src.app.db.models.business_orm import BusinessORM

class BusinessMariaDbMapper(Mapper[BusinessORM, Business]):
    def mapToDomain(self, param: BusinessORM) -> Business:
        return Business(**param.asdict())

    def mapToDomainList(self, params: list[BusinessORM]) -> list[Business]:
        entities: list[Business]
        for param in params:
            entities.append(self.mapToDomain(param))
        return entities

    def mapFromDomain(self, param: Business) -> BusinessORM:
        return BusinessORM(
            **param.as_dict()
        )

    def mapFromDomainList(self, params: list[Business]) -> list[BusinessORM]:
        orms: list[BusinessORM]
        for param in params:
            orms.append(self.mapFromDomain(param))
        return orms
