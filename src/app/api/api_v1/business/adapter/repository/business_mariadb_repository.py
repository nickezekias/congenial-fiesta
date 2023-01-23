from sqlalchemy.orm import Session

from src.app.db.repository import Repository
from src.domain.business.i_business_repository import IBusinessRepository
from src.app.api.api_v1.business.adapter.repository.business_mariadb_mapper import BusinessMariaDbMapper


from src.domain.business.business import Business
from src.app.db.models.business_orm import BusinessORM

class BusinessMariaDbRepository(Repository[BusinessORM, Business], IBusinessRepository):
    db: Session
    mapper: BusinessMariaDbMapper

    def __init__(self, db: Session, mapper = BusinessMariaDbMapper()) -> None:
        super().__init__(db, mapper)
        self.db = db
        self.mapper = mapper

    def find_locations(self):
        pass

    def update(self, business: Business) -> Business:
        pass