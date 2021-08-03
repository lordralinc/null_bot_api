import asyncio
from abc import ABC, abstractmethod


class NullBotAPIABC(ABC):

    @property
    @abstractmethod
    def api_instance(self) -> "NullBotAPIABC":
        ...

    @abstractmethod
    def make_request(
            self,
            method: str,
            data=None
    ) -> dict:
        ...

    @abstractmethod
    async def make_request_async(
            self,
            method: str,
            data=None
    ) -> dict:
        ...

    @property
    @abstractmethod
    def loop(self) -> asyncio.AbstractEventLoop:
        ...


class BaseAPICategoriesABC(ABC):
    ...


class APICategoriesABC(ABC):

    @property
    @abstractmethod
    def experts(self) -> "BaseAPICategoriesABC":
        ...
