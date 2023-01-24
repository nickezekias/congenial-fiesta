from abc import abstractmethod

from src.domain.base.i_repository import IRepository
from src.domain.business.business import Business
from src.app.db.models.business_orm import BusinessORM

class IBusinessRepository(IRepository[BusinessORM, Business]):

    @abstractmethod
    def find_locations(self):
        pass
