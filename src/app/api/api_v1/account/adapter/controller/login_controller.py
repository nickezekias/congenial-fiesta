from datetime import datetime, timedelta
from src.app.api.api_v1.account.adapter.request.login_request import LoginRequest
from src.app.api.api_v1.account.use_cases.login import Login as LoginUseCase
from src.app.api.api_v1.account.adapter.presenter.login_presenter import LoginPresenter

from src.domain.account.i_account_repository import IAccountRepository
from src.domain.account.i_authenticator import IAuthenticator



class LoginController:
    account_repository: IAccountRepository
    authenticator: IAuthenticator

    def __init__(self, account_repository: IAccountRepository, authenticator: IAuthenticator) -> None:
        self.account_repository = account_repository
        self.authenticator = authenticator

    async def login(self, form_data: LoginRequest, access_token_expires: timedelta) -> dict | None:
        return await LoginUseCase(self.account_repository, LoginPresenter(), self.authenticator).execute(form_data, access_token_expires)

    


