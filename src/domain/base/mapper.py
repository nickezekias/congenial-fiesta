from abc import ABC, abstractmethod
from typing import Generic, TypeVar

I = TypeVar('I')
O = TypeVar('O')

class Mapper(ABC, Generic[I, O]):
    """ Map from external input to domain """
    @abstractmethod
    def mapToDomain(self, param: I) -> O:
        pass

    # @abstractmethod
    # def mapToDomainList(self, params: list[I]) -> list[O]:
    #     pass
    
    """ Map from domain model to external input format """
    @abstractmethod
    def mapFromDomain(self, param: O) -> I:
        pass

    # @abstractmethod
    # def mapFromDomainList(self, params: list[O]) -> list[I]:
    #     pass