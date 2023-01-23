from dataclasses import dataclass
from src.domain.base.i_use_case import IUseCase
from src.domain.account.i_authenticator import IAuthenticator

from src.domain.account.i_account_presenter import IAccountPresenter
from src.domain.account.i_account_repository import IAccountRepository
from src.domain.util.i_crypto import ICrypto

class ResetPassword(IUseCase):
    repository: IAccountRepository
    presenter: IAccountPresenter
    crypto: ICrypto
    authenticator: IAuthenticator

    def __init__(
        self,
        repository: IAccountRepository,
        presenter: IAccountPresenter,
        crypto: ICrypto,
        authenticator: IAuthenticator
    ) -> None:
        self.repository = repository
        self.presenter = presenter
        self.crypto = crypto
        self.authenticator = authenticator

    @dataclass
    class Request:
        token: str
        email: str
        password: str
        password_confirmation: str

    @dataclass
    class Response:
        success: bool
        message: str

    async def execute(self, payload: Request) -> Response:
        # return { "success": True, "message": payload.token }
        email = self.crypto.verify_token(payload.token)
        # return { "success": True, "message": email }
        if not email:
            self.presenter.output_error_invalid_token()
        
        user = self.repository.get_by_email(email)
        if not user:
            self.presenter.output_error_user_not_found()

        password = self.authenticator.get_password_hash(payload.password)
        user.password = password
        user.first_name = "Nick"
        user.last_name = "Arts"
        self.repository.update(user)
        self.repository.commit()
        return self.presenter.output_reset_password()

        


