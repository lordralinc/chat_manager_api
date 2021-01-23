import asyncio
from abc import ABC, abstractmethod
from typing import TypeVar, Type, Optional

from pydantic import BaseModel

T = TypeVar('T', dict, BaseModel, str)


class ChatManagerAPIABC(ABC):

    @property
    @abstractmethod
    def api_instance(self) -> "ChatManagerAPIABC":
        ...

    @abstractmethod
    def make_request(self, method: str, data: Optional[dict] = None, dataclass: Type[T] = dict) -> T:
        ...

    @abstractmethod
    async def make_request_async(self, method: str, data: Optional[dict] = None, dataclass: Type[T] = dict) -> T:
        ...

    @property
    @abstractmethod
    def loop(self) -> asyncio.AbstractEventLoop:
        ...


class BaseAPICategoryABC(ABC):
    ...


class APICategoriesABC(ABC):

    @property
    @abstractmethod
    def api_instance(self) -> "ChatManagerAPIABC":
        ...
