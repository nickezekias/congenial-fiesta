from abc import abstractmethod

from src.domain.base.i_repository import IRepository
from src.domain.account.user import User

class IAccountRepository(IRepository[User]):
    @abstractmethod
    def get_by_email(self, email: str) -> User | None:
        pass

    # def isAuthenticated
    
    # def getCurrentUser

    # def forgotPassword

    # def logout
    
    