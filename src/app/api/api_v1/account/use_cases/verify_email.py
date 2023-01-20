from src.domain.base.i_use_case import IUseCase
from src.domain.account.i_account_presenter import IAccountPresenter
from src.domain.account.i_account_repository import IAccountRepository
from src.domain.util.i_crypto import ICrypto
from src.app.api.api_v1.account.adapter.request.verify_email_request import VerifyEmailRequest

from src.domain.account.user import User

class VerifyEmail(IUseCase):
    repository: IAccountRepository
    presenter: IAccountPresenter
    crypto: ICrypto

    def __init__(
            self,
            repository: IAccountRepository,
            presenter: IAccountPresenter,
            crypto: ICrypto,
        ) -> None:
        self.repository = repository
        self.presenter = presenter
        self.crypto = crypto

    async def execute(self, payload: VerifyEmailRequest) -> dict:
        user: User = self.repository.get_by_email(payload.email)
        if not user:
            self.presenter.output_error_login_to_verify_email()

        email_from_token = self.crypto.verify_token(payload.token, subject="email")
        if not email_from_token:
            self.presenter.output_error_invalid_email_verification_link()

        if email_from_token == payload.email:
            return self.presenter.output_verify_email()
        else:
            self.presenter.output_error_invalid_email_verification_link()
        