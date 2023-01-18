from dataclasses import asdict

from src.domain.base.mapper import Mapper
from src.domain.business.business import Business
from src.domain.business.workspace import Workspace
from src.app.db.models.business_orm import BusinessORM

from src.app.util.date_time_util import DateTimeUtil

class BusinessMariaDbMapper(Mapper[BusinessORM, Business]):
    def mapToDomain(self, param: BusinessORM) -> Business:
        return Business(
            id = param.id,
            annual_turnover = param.annual_turnover,
            business_model = param.business_model,
            company_size = param.company_size,
            company_type = param.company_type,
            description = param.description,
            employees = param.employees.split(','),
            ID_document = param.ID_document,
            ID_document_verified_at = param.ID_document_verified_at,
            industry = param.industry,
            investors = param.investors.split(','),
            locations = param.locations.split(','),
            markets = param.markets.split(','),
            name = param.name,
            org_type = param.org_type,
            partners = param.partners.split(','),
            payment = param.payment,
            payment_verified_at = param.payment_verified_at,
            pitch_deck = param.pitch_deck,
            products = param.products.split(','),
            projects = param.projects.split(','),
            sector = param.sector,
            website = param.website,
            workspace = Workspace(**param.workspace),
            year_founded = param.year_founded,
            created_at = DateTimeUtil.string_to_date(param.created_at),
            updated_at = DateTimeUtil.string_to_date(param.updated_at)
        )

    def mapToDomainList(self, params: list[BusinessORM]) -> list[Business]:
        entities: list[Business]
        for param in params:
            entities.append(self.mapToDomain(param))
        return entities

    def mapFromDomain(self, param: Business) -> BusinessORM:
        return BusinessORM(
            id = param.id,
            annual_turnover = param.annual_turnover,
            business_model = param.business_model,
            company_size = param.company_size,
            company_type = param.company_type,
            description = param.description,
            employees = ','.join(param.employees),
            ID_document = param.ID_document,
            ID_document_verified_at = param.ID_document_verified_at,
            industry = param.industry,
            investors = ','.join(param.investors),
            locations = ','.join(param.locations),
            markets = ','.join(param.markets),
            name = param.name,
            org_type = param.org_type,
            partners = ','.join(param.partners),
            payment = param.payment,
            payment_verified_at = param.payment_verified_at,
            pitch_deck = param.pitch_deck,
            products = ','.join(param.products),
            projects = ','.join(param.projects),
            sector = param.sector,
            website = param.website,
            workspace = param.workspace.as_dict(),
            year_founded = param.year_founded,
            created_at = DateTimeUtil.date_to_iso_string(param.created_at),
            updated_at = DateTimeUtil.date_to_iso_string(param.updated_at)
        )

    def mapFromDomainList(self, params: list[Business]) -> list[BusinessORM]:
        orms: list[BusinessORM]
        for param in params:
            orms.append(self.mapFromDomain(param))
        return orms
