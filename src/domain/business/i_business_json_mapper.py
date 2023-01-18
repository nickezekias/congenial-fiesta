from abc import ABC, abstractmethod

from src.domain.business.business import Business
from src.app.api.api_v1.business.adapter.request.business_request import BusinessPostRequest
from src.app.api.api_v1.business.adapter.response.business_response import BusinessPostResponse

class IBusinessJsonMapper(ABC):
    @abstractmethod
    def mapToDomain(self, param: BusinessPostRequest) -> Business:
        pass

    @abstractmethod
    def mapFromDomain(self, param: Business) -> BusinessPostResponse:
        pass
