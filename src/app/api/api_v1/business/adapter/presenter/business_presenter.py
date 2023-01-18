from src.domain.business.i_business_presenter import IBusinessPresenter
from src.domain.business.business import Business
from src.app.api.api_v1.business.adapter.response.business_response import BusinessPostResponse
from src.app.api.api_v1.business.adapter.presenter.business_json_mapper import BusinessJsonMapper

class BusinessPresenter(IBusinessPresenter):
    def output(self, param: Business) -> BusinessPostResponse:
        mapper = BusinessJsonMapper()
        return mapper.mapFromDomain(param)
