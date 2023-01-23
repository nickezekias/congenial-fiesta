from abc import ABC, abstractmethod


class IAccountPresenter(ABC):
    #shared
    @abstractmethod
    def output_error_user_not_found(self) -> None:
        pass



    # verify email outputs -----------------------------------------------
    @abstractmethod
    def output_verify_email(self) -> dict:
        pass

    # verify email error outputs -------------
    @abstractmethod
    def output_error_login_to_verify_email(self) -> None:
        pass
    
    @abstractmethod
    def output_error_invalid_email_verification_link(self) -> None:
        pass



    # forgot password
    @abstractmethod
    def output_forgot_password(self) -> None:
        pass

    # reset password
    @abstractmethod
    def output_error_invalid_token(self) -> None:
        pass

    @abstractmethod
    def output_reset_password(self) -> dict:
        pass