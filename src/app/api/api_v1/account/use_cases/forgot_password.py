from src.domain.base.i_use_case import IUseCase
from src.domain.account.i_account_presenter import IAccountPresenter
from src.domain.account.i_account_repository import IAccountRepository
from src.domain.util.i_crypto import ICrypto
from src.domain.notification.notification import Notification

from src.domain.account.user import User

class ForgotPassword(IUseCase):
    repository: IAccountRepository
    presenter: IAccountPresenter
    crypto: ICrypto
    notification: Notification

    def __init__(
            self,
            repository: IAccountRepository,
            presenter: IAccountPresenter,
            crypto: ICrypto,
            notification: Notification
        ) -> None:
        self.repository = repository
        self.presenter = presenter
        self.crypto = crypto
        self.notification = notification

    async def execute(self, email: str) -> dict:
        user: User = self.repository.get_by_email(email)
        if not user:
            self.presenter.output_error_user_not_found()

        token = self.crypto.generate_token(
            subject=user.email,
            expires_type="minutes",
            expires_duration=60
        )
        # init and send  notification
        self.notification.notifiable = user
        self.notification.token = token
        await self.notification.send()

        return self.presenter.output_forgot_password()
