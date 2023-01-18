from abc import abstractmethod

from src.domain.base.i_repository import IRepository
from src.domain.business.business import Business

class IBusinessRepository(IRepository[Business]):

    @abstractmethod
    def find_locations(self):
        pass
