from abc import ABC, abstractmethod
from typing import TypeVar

from src.domain.base.i_presenter import IPresenter

I = TypeVar('I')
O = TypeVar('O')

class IBusinessPresenter(ABC):
    @abstractmethod
    def output(self, data: I) -> O:
        pass
