from src.domain.account.i_authenticator import IAuthenticator
from src.domain.notification.notification import Notification
from src.domain.util.i_crypto import ICrypto

from src.domain.account.i_account_repository import IAccountRepository
from src.domain.account.i_register_presenter import IRegisterPresenter

from src.domain.business.i_business_repository import IBusinessRepository
from src.domain.business.i_business_presenter import IBusinessPresenter
from src.app.api.api_v1.account.adapter.request.register_request import RegisterRequest


from src.app.api.api_v1.account.use_cases.register import Register as RegisterUseCase
from src.app.api.api_v1.account.adapter.response.register_response import RegisterResponse

class RegisterController:
    account_repository: IAccountRepository
    register_presenter: IRegisterPresenter
    business_repository: IBusinessRepository
    business_presenter: IBusinessPresenter
    authenticator: IAuthenticator
    notification: Notification
    crypto: ICrypto
    def __init__(
        self,
        account_repository: IAccountRepository,
        register_presenter: IRegisterPresenter,
        business_repository: IBusinessRepository,
        business_presenter: IBusinessPresenter,
        authenticator: IAuthenticator,
        notification: Notification,
        crypto: ICrypto
    ) -> None:
        self.account_repository = account_repository
        self.register_presenter = register_presenter
        self.business_repository = business_repository
        self.business_presenter = business_presenter
        self.authenticator = authenticator
        self.notification = notification
        self.crypto = crypto

    async def register(self, form_data: RegisterRequest) -> RegisterResponse | None:
        return await RegisterUseCase(
            account_repository = self.account_repository,
            register_presenter = self.register_presenter,
            business_repository = self.business_repository,
            business_presenter = self.business_presenter,
            authenticator=self.authenticator,
            notification=self.notification,
            crypto = self.crypto
        ).execute(form_data)
