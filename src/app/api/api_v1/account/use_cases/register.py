from src.domain.account.i_register_presenter import IRegisterPresenter
from src.domain.base.i_use_case import IUseCase
from src.domain.account.i_authenticator import IAuthenticator

from src.domain.account.user import User
from src.domain.account.i_account_repository import IAccountRepository
from src.app.api.api_v1.account.adapter.presenter.account_json_mapper import AccountJsonMapper
from src.app.api.api_v1.account.adapter.request.register_request import RegisterRequest

from src.domain.business.business import Business
from src.domain.business.i_business_repository import IBusinessRepository
from src.domain.business.i_business_presenter import IBusinessPresenter
from src.app.api.api_v1.business.adapter.presenter.business_json_mapper import BusinessJsonMapper

from src.app.api.api_v1.account.adapter.response.register_response import RegisterResponse
class Register(IUseCase):
    account_repository: IAccountRepository
    register_presenter: IRegisterPresenter
    business_repository: IBusinessRepository
    business_presenter: IBusinessPresenter
    authenticator: IAuthenticator
    account_json_mapper: AccountJsonMapper
    business_json_mapper: BusinessJsonMapper

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

    async def execute(self, form_data: RegisterRequest) -> RegisterResponse | None:
        # create user entity from form data
        user_req = form_data.user
        user_req.password = self.authenticator.get_password_hash(user_req.password) # hash user request password
        user_input = self.account_json_mapper.mapToDomain(user_req)

        # create business entity from form_data
        business_req = form_data.business
        business_input = self.business_json_mapper.mapToDomain(business_req)

        # check no user with same email exists
        found_user: User = self.account_repository.get_by_email(email = user_input.email)
        if found_user:
            self.register_presenter.output_error_email_exists()

        # add user to DB
        user: User = self.account_repository.add(entity=user_input)

        # add business to db and get presented data
        business: Business = self.business_repository.add(entity=business_input)

        # []FIXME: use unit-of-work to commit application transactions
        # commit transaction to db
        self.account_repository.commit()
        return self.register_presenter.output(user, business)