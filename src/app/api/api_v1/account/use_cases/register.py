from src.domain.account.i_register_presenter import IRegisterPresenter
from src.domain.base.i_use_case import IUseCase
from src.domain.account.i_authenticator import IAuthenticator

from src.domain.account.user import User
from src.domain.account.i_account_repository import IAccountRepository

from src.domain.business.business import Business
from src.domain.business.i_business_repository import IBusinessRepository
from src.domain.business.i_business_presenter import IBusinessPresenter
from src.app.api.api_v1.business.adapter.response.business_response import BusinessPostResponse

from src.app.api.api_v1.business.use_cases.create_business import CreateBusiness as CreateBusinessUseCase
from src.app.api.api_v1.account.adapter.response.register_response import RegisterResponse

class Register(IUseCase):
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

    async def execute(self, user: User, business: Business) -> RegisterResponse | None:
        found_user: User = self.account_repository.get_by_email(email = user.email)
        if found_user:
            self.register_presenter.output_error_email_exists()
        new_user = self.account_repository.add(entity=user, NO_COMMIT=True)
        business_res: BusinessPostResponse = await CreateBusinessUseCase(
            self.business_repository,
            self.business_presenter
        ).execute(business)
        # []FIXME: use unit-of-work to commit application transactions
        self.business_repository.commit()
        return self.register_presenter.output(new_user, business_res)