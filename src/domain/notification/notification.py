from abc import ABC, abstractmethod
from enum import Enum
from typing import Generic, TypeVar

TEntity = TypeVar("TEntity")

class Notification(ABC, Generic[TEntity]):
    _notifiable: TEntity

    """ Possible channels on which to send notifications """
    class Channels(Enum):
        DATABASE = 1
        EMAIL = 2
        SMS = 3

    """The channel by which the email is sent: mail, database, sms, ..."""
    #[]FIXME: create an enum class for channels
    channel: Channels = Channels.EMAIL

    @property
    def notifiable(self) -> TEntity:
        return self._notifiable

    @notifiable.setter
    def notifiable(self, value: TEntity) -> None:
        self._notifiable = value

    @abstractmethod    
    def via(self, channels: list[Channels] = [Channels.EMAIL]):
        pass

    """ def to_array(entity: TEntity):
        pass """

    @abstractmethod
    def to_mail():
        pass

    """ def to_sms(entity: TEntity):
        pass """

    @abstractmethod
    def send(self):
        pass