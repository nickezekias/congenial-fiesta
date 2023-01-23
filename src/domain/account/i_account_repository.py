from abc import abstractmethod

from src.domain.base.i_repository import IRepository
from src.domain.account.user import User
from src.app.db.models.user_orm import UserORM

class IAccountRepository(IRepository[UserORM, User]):
    @abstractmethod
    def get_by_email(self, email: str) -> User | None:
        pass

    # def isAuthenticated
    
    # def getCurrentUser

    # def forgotPassword

    # def logout
    
    