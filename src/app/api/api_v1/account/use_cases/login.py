from src.domain.base.i_use_case import IUseCase
from src.domain.account.i_authenticator import IAuthenticator
from src.domain.account.i_account_repository import IAccountRepository
from src.domain.account.i_login_presenter import ILoginPresenter

class Login(IUseCase):
    repository: IAccountRepository
    presenter: ILoginPresenter
    authenticator: IAuthenticator

    def __init__(self, repository: IAccountRepository, presenter: ILoginPresenter, authenticator: IAuthenticator) -> None:
        super().__init__()
        self.repository = repository
        self.presenter = presenter
        self.authenticator = authenticator

    async def execute(self, email: str, password: str) -> dict | None:
        user = self.repository.get_by_email(email)
        if not user:
            self.presenter.output_error_user_not_found()
        if not self.authenticator.verify_password(password, user.password):
            self.presenter.output_error_user_not_found()
        return self.presenter.output({"token": "77483237"})
