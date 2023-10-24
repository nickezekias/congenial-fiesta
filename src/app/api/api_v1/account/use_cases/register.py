from src.domain.account.i_register_presenter import IRegisterPresenter
from src.domain.base.i_use_case import IUseCase
from src.domain.account.i_authenticator import IAuthenticator
from src.domain.notification.notification import Notification
from src.domain.util.i_crypto import ICrypto
from src.app.core.utils.constants import TokenLabels

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
        self.account_json_mapper = AccountJsonMapper()
        self.business_json_mapper = BusinessJsonMapper()
        self.notification = notification
        self.crypto = crypto

    async def execute(self, form_data: RegisterRequest) -> RegisterResponse | None:
        # create user entity from form data
        user_req = form_data.user
        user_req.password = self.authenticator.get_password_hash(user_req.password) # hash user request password
        user_input = self.account_json_mapper.mapToDomain(user_req)
        user_input.is_active = False

        # create business entity from form_data
        business_req = form_data.business
        business_input = self.business_json_mapper.mapToDomain(business_req)

        # check no user with same email exists
        found_user: User = self.account_repository.get_by_email(email = user_input.email)
        if found_user:
            return self.register_presenter.output_errors_email_exists()
        
        # check no user with same email exists
        found_user: User = self.account_repository.get_by_phone(phone = user_input.phone)
        if found_user:
            return self.register_presenter.output_errors_phone_exists()

        # add user to DB
        # user_input.token = self.authenticator.create_access_token(subject=user_req.email)
        self.account_repository.add(entity=user_input)

        # add business to db and get presented data
        self.business_repository.add(entity=business_input)

        # []FIXME: use unit-of-work to commit application transactions
        # commit transaction to db
        try:
            self.account_repository.commit()
            #hydrate object with saved user
            user: User = self.account_repository.get_by_email(user_input.email)
            business: Business = self.business_repository.get(business_input.id)


            #init and send new account notification
            token = self.crypto.generate_token(
                subject=user.email,
                expires_type="minutes",
                expires_duration=30
            )
            self.notification.notifiable = user
            self.notification.token = token
            await self.notification.send()

            return self.register_presenter.output(user, business)
        except:
            self.register_presenter.output_errors_invalid_data()

