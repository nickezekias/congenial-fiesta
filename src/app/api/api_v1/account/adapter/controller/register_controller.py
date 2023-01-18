from src.domain.account.i_authenticator import IAuthenticator

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
    def __init__(
        self,
        account_repository: IAccountRepository,
        register_presenter: IRegisterPresenter,
        business_repository: IBusinessRepository,
        business_presenter: IBusinessPresenter,
        authenticator: IAuthenticator
    ) -> None:
        self.account_repository = account_repository
        self.register_presenter = register_presenter
        self.business_repository = business_repository
        self.business_presenter = business_presenter
        self.authenticator = authenticator

    async def register(self, form_data: RegisterRequest) -> RegisterResponse | None:
        return await RegisterUseCase(
            account_repository = self.account_repository,
            register_presenter = self.register_presenter,
            business_repository = self.business_repository,
            business_presenter = self.business_presenter,
            authenticator=self.authenticator
        ).execute(form_data)
