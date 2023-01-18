from sqlalchemy.orm import Session

from src.app.db.repository import Repository
from src.domain.account.i_account_repository import IAccountRepository
from src.app.api.api_v1.account.adapter.repository.account_mariadb_mapper import AccountMariaDbMapper

from src.domain.account.user import User
from src.app.db.models.user_orm import UserORM

class AccountMariaDbRepository(Repository[User], IAccountRepository):
    db: Session
    mapper: AccountMariaDbMapper

    def __init__(self, db: Session, mapper = AccountMariaDbMapper()) -> None:
        super().__init__(db, mapper)
        self.db = db
        self.mapper = mapper

    def get_by_email(self, email: str) -> User | None:
        orm = self.db.query(UserORM).filter(UserORM.email == email).first()
        if orm:
            return self.mapper.mapToDomain(orm)
        return None