from fastapi import HTTPException

from src.domain.account.i_register_presenter import IRegisterPresenter
from src.domain.account.user import User

from src.app.api.api_v1.account.adapter.presenter.account_json_mapper import AccountJsonMapper
from src.app.api.api_v1.business.adapter.response.business_response import BusinessPostResponse
from src.app.api.api_v1.account.adapter.response.register_response import RegisterResponse

class RegisterPresenter(IRegisterPresenter):

    def output(self, user: User, business_res: BusinessPostResponse) -> RegisterResponse:
        user_res = AccountJsonMapper().mapFromDomain(user)
        return {
            "user": user_res,
            "business": business_res
        }

    def output_error_email_exists(self) -> None:
        raise HTTPException(
            status_code=400,
            detail="account.register.error.emailExists"
        )