from src.domain.account.i_authenticator import IAuthenticator

from src.domain.account.i_account_repository import IAccountRepository
from src.domain.account.i_register_presenter import IRegisterPresenter
from src.app.api.api_v1.account.adapter.presenter.account_json_mapper import AccountJsonMapper

from src.domain.business.i_business_repository import IBusinessRepository
from src.domain.business.i_business_presenter import IBusinessPresenter
from src.app.api.api_v1.account.adapter.request.register_request import RegisterRequest
from src.app.api.api_v1.business.adapter.presenter.business_json_mapper import BusinessJsonMapper


from src.app.api.api_v1.account.use_cases.register import Register as RegisterUseCase
from src.app.api.api_v1.account.adapter.response.register_response import RegisterResponse

class RegisterController:
    account_repository: IAccountRepository
    register_presenter: IRegisterPresenter
    business_repository: IBusinessRepository
    business_presenter: IBusinessPresenter
    account_json_mapper: AccountJsonMapper
    business_json_mapper: BusinessJsonMapper
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
        self.account_json_mapper = AccountJsonMapper()
        self.business_json_mapper = BusinessJsonMapper()

    async def register(self, form_data: RegisterRequest) -> RegisterResponse | None:
        user_req = form_data.user
        user_req.password = self.authenticator.get_password_hash(user_req.password)
        user = self.account_json_mapper.mapToDomain(user_req)
        business_req = form_data.business
        business = self.business_json_mapper.mapToDomain(business_req)
        return await RegisterUseCase(
            account_repository = self.account_repository,
            register_presenter = self.register_presenter,
            business_repository = self.business_repository,
            business_presenter = self.business_presenter,
            authenticator=self.authenticator
        ).execute(user, business)
