from fastapi import HTTPException

from src.domain.account.i_account_presenter import IAccountPresenter

class AccountPresenter(IAccountPresenter):


    def output_verify_email(self) -> dict:
        return {
            "success": True,
            "message": "account.verifyEmail.success"
        }

    def output_error_login_to_verify_email(self) -> None:
        raise HTTPException(
            status_code=400,
            detail="account.verifyEmail.loginToVerifyEmail"
        )

    def output_error_invalid_email_verification_link(self) -> None:
        raise HTTPException(
            status_code=400,
            detail="account.verifyEmail.invalidVerificationLink"
        )