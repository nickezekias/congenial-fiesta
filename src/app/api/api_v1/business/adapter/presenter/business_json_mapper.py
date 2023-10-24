from datetime import datetime

from src.domain.business.i_business_json_mapper import IBusinessJsonMapper
from src.domain.business.business import Business
from src.domain.business.workspace import Workspace
from src.app.api.api_v1.business.adapter.request.business_request import BusinessPostRequest
from src.app.api.api_v1.business.adapter.response.business_response import BusinessPostResponse

from src.app.util.date_time_util import DateTimeUtil

class BusinessJsonMapper(IBusinessJsonMapper):

    def mapToDomain(self, param: BusinessPostRequest) -> Business:
        now = datetime.now()
        #FIXME: entity id is implicitly generated by base entity class
        #FIX: make this explicit with say a factory pattern
        return Business(
            id = "",
            annual_turnover = "",
            business_model = "",
            company_size = param.company_size,
            company_type = param.company_type,
            description = param.description,
            employees = [],
            ID_document = "",
            ID_document_verified_at = None,
            industry = param.industry,
            investors = [],
            locations = [],
            markets = [],
            name = param.name,
            org_type = param.org_type,
            partners = [],
            payment = None,
            payment_verified_at = None,
            pitch_deck = "",
            products = [],
            projects = [],
            sector = param.sector,
            website = param.website,
            workspace = Workspace(**param.workspace),
            year_founded = param.year_founded,
            created_at = now,
            updated_at = now
        )

    def mapFromDomain(self, param: Business) -> BusinessPostResponse:
        return BusinessPostResponse(
            id = param.id,
            annual_turnover = param.annual_turnover,
            business_model = param.business_model,
            company_size = param.company_size,
            company_type = param.company_type,
            description = param.description,
            employees = param.employees,
            ID_document = param.ID_document,
            ID_document_verified_at = param.ID_document_verified_at,
            industry = param.industry,
            investors = param.investors,
            locations = param.locations,
            markets = param.markets,
            name = param.name,
            org_type = param.org_type,
            partners = param.partners,
            payment = param.payment,
            payment_verified_at = param.payment_verified_at,
            pitch_deck = param.pitch_deck,
            products = param.products,
            projects = param.projects,
            sector = param.sector,
            website = param.website,
            workspace = param.workspace.as_dict(),
            year_founded = DateTimeUtil.date_to_string(param.year_founded),
            created_at = DateTimeUtil.date_to_string(param.created_at),
            updated_at = DateTimeUtil.date_to_string(param.updated_at)
        )