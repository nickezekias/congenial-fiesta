from fastapi import HTTPException

from src.domain.account.i_login_presenter import ILoginPresenter

class LoginPresenter(ILoginPresenter):
    def output(self, data: dict) -> dict[str, str]:
        return {
            "token": data["token"]
        }

    def output_error_user_not_found(self) -> None:
        raise HTTPException(
            status_code = 404,
            detail = "account.login.error.userNotFound"
        )
