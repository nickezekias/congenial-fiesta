from fastapi import HTTPException

from src.domain.account.i_register_presenter import IRegisterPresenter
from src.domain.account.user import User

from src.app.api.api_v1.business.adapter.presenter.business_json_mapper import BusinessJsonMapper
from src.app.api.api_v1.account.adapter.presenter.account_json_mapper import AccountJsonMapper
from src.app.api.api_v1.business.adapter.response.business_response import BusinessPostResponse
from src.app.api.api_v1.account.adapter.response.register_response import RegisterResponse

class RegisterPresenter(IRegisterPresenter):

    def output(self, user: User, business: BusinessPostResponse) -> RegisterResponse:
        user_res = AccountJsonMapper().mapFromDomain(user)
        business_res = BusinessJsonMapper().mapFromDomain(business)
        return {
            "user": user_res,
            "business": business_res
        }

    def output_errors_email_exists(self) -> None:
        raise HTTPException(
            status_code=400,
            detail="account.register.errors.emailExists"
        )
    
    def output_errors_phone_exists(self) -> None:
        raise HTTPException(
            status_code=400,
            detail="account.register.errors.phoneExists"
        )
    
    def output_errors_user_data_duplicate(self) -> None:
        raise HTTPException(
            status_code=400,
            detail="account.register.errors.userDataDuplicate"
        )
    
    def output_errors_invalid_data(self) -> None:
        raise HTTPException(
            status_code=400,
            detail="account.register.errors.invalidData"
        )