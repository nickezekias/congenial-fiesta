from abc import ABC, abstractmethod
from typing import TypeVar

TUserEntity = TypeVar('TUserEntity')
TBusinessPostResponse = TypeVar('TBusinessPostResponse')
TRegisterResponse = TypeVar('TRegisterResponse')

class IRegisterPresenter(ABC):

    @abstractmethod
    def output(self, user: TUserEntity, business_res: TBusinessPostResponse) -> TRegisterResponse:
        pass

    @abstractmethod
    def output_error_email_exists(self) -> None:
        pass