import asyncio
from typing import Type, TypeVar, Dict

import urllib
import aiohttp
import requests
from attrdict import AttrDict
from pydantic import BaseModel, ValidationError

from null_bot_api import const
from null_bot_api.abc import NullBotAPIABC
from null_bot_api.categories import APICategories
from null_bot_api.exceptions import NullBotAPIException

try:
    from loguru import logger
except ImportError:
    import logging

    logger = logging.getLogger(__name__)

T = TypeVar('T', dict, AttrDict, BaseModel)


class NullBotAPI(NullBotAPIABC, APICategories):
    URL = "https://c3po.ru/api/{method}"

    @property
    def api_instance(self) -> "NullBotAPI":
        return self

    def __init__(
            self,
            loop: asyncio.AbstractEventLoop = None,
            raise_validation_error: bool = False,
            timeout: float = 30,
    ):
        self._loop = loop
        self.raise_validation_error = raise_validation_error
        self.timeout = timeout

    def __repr__(self) -> str:
        return (
            f"<NullBotAPI("
            f"raise_validation_error={self.raise_validation_error}, "
            f"timeout={self.timeout}, "
            f")>"
        )

    @staticmethod
    def prepare_data(data: dict) -> str:
        new_data = {}
        for k, v in data.items():
            if isinstance(v, list) or isinstance(v, tuple):
                new_data[k] = ",".join([str(li) for li in v])
            else:
                new_data[k] = v
        return "?" + urllib.parse.urlencode(new_data) if new_data else ""

    def make_request(self, method: str, data=None, dataclass: Type[T] = AttrDict) -> T:
        """Выполняет запрос к серверу NullBotAPI

        :param method: Название метода
        :param data: Параметры
        :param dataclass: Датакласс, который влияет на тип выходного значения
        :return: Результат запроса
        """
        if data is None:
            data = dict()

        request_url = self.URL.format(method=method)
        logger.debug(
            f"Make GET request to {request_url} with data {self.data_to_print(data)}. Timeout {self.timeout}"
        )
        response = requests.get(request_url + self.prepare_data(data), timeout=self.timeout)
        response.raise_for_status()
        response_json = response.json()
        logger.debug(f"Response: {response_json}. Use dataclass {dataclass.__name__}.")
        return self.validate_response(response_json, dataclass)

    async def make_request_async(self, method: str, data=None, dataclass: Type[T] = AttrDict) -> T:
        """Выполняет запрос к серверу NullBotAPI (асинхронно)
        :param method: Название метода
        :param data: Параметры
        :param dataclass: Датакласс, который влияет на тип выходного значения
        :return: Результат запроса
        """
        if data is None:
            data = dict()

        request_url = self.URL.format(method=method)
        logger.debug(
            f"Make async GET request to {request_url} with data {self.data_to_print(data)}. Timeout {self.timeout}"
        )
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=self.timeout)) as session:
            async with session.get(request_url + self.prepare_data(data)) as response:
                response.raise_for_status()
                response_json = await response.json()
                logger.debug(f"Response: {response_json}.")
                return self.validate_response(response_json, dataclass)

    def validate_response(self, response: Dict, dataclass: Type[T]) -> T:
        if isinstance(response, int):
            raise NullBotAPIException(error=response)
        if 'error' in response:
            raise NullBotAPIException(**response)
        try:
            data = dataclass(**response)
            logger.debug(f"Response validated with dataclass {dataclass.__name__}")
            return data
        except ValidationError as ex:
            if self.raise_validation_error:
                raise ex
            logger.error(f"Response validated with dataclass AttrDict")
            return AttrDict(response)

    @staticmethod
    def data_to_print(data: Dict) -> Dict:
        new_dict = {}
        for k, v in data.items():
            if k == 'access_token':
                new_dict[k] = v[:4] + '*' * 4 + v[-4:]
            else:
                new_dict[k] = v
        return new_dict

    @property
    def loop(self) -> asyncio.AbstractEventLoop:
        if self._loop is None:
            self._loop = asyncio.get_event_loop()
        return self._loop

    @loop.setter
    def loop(self, new_loop: asyncio.AbstractEventLoop):
        self._loop = new_loop

    @property
    def author(self) -> str:
        return const.__author__

    @property
    def version(self) -> str:
        return const.__version__
