from typing import Union, Type, TypeVar, Dict, Optional

import requests
import asyncio
import aiohttp
from pydantic import BaseModel

from chat_manager_api.abc import ChatManagerAPIABC
from chat_manager_api.categories import APICategories
from chat_manager_api.exceptions import ChatManagerAPIException

import logging

logger = logging.getLogger(__name__)

T = TypeVar('T', dict, BaseModel, str)


class ChatManagerAPI(ChatManagerAPIABC, APICategories):
    URL = "https://api.chatmanager.pro/"

    @property
    def api_instance(self) -> "ChatManagerAPI":
        return self

    def __init__(
            self,
            token: str,
            loop: asyncio.AbstractEventLoop = None
    ):
        self._token = token
        self._loop = loop

    @property
    def headers(self) -> Dict[str, str]:
        return {
            "accept": "text/html,application/xhtml+xml,application/xml;"
                      "q=0.9,image/avif,image/webp,image/apng,*/*;"
                      "q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/74.0.3729.169 Safari/537.36"
        }

    def _get_link(self, method: str, data: dict = None) -> str:
        if data is None:
            data = {}
        data.update(token=self._token, method=method)

        url = ChatManagerAPI.URL
        return url + "?" + "&".join([f"{k}={v}" for k, v in data.items()])

    def _do_pre(self, method: str, data: dict = None) -> str:
        link = self._get_link(method, data)
        logger.debug(f"Do request to {link}")
        return link

    @staticmethod
    def _do_post(response: dict, cls: Type[T] = dict) -> T:
        logger.debug(f"Response: {response}. Use dataclass: {cls.__name__}")
        if 'error' in response:
            raise ChatManagerAPIException(
                **response
            )
        _response = response.get('response', {})
        if isinstance(_response, str):
            return _response
        return cls(**_response)

    def make_request(self, method: str, data: Optional[dict] = None, dataclass: Type[T] = dict) -> T:
        """Выполняет запрос к серверу

        :param method: Название метода
        :param data: Параметры
        :param dataclass: Датакласс, который влияет на тип выходного значения
        :return: Результат запроса
        """
        link = self._do_pre(method, data)
        response = requests.get(link, headers=self.headers).json()
        return self._do_post(response, dataclass)

    async def make_request_async(self, method: str, data: Optional[dict] = None, dataclass: Type[T] = dict) -> T:
        """Выполняет запрос к серверу (асинхронно)

        :param method: Название метода
        :param data: Параметры
        :param dataclass: Датакласс, который влияет на тип выходного значения
        :return: Результат запроса
        """
        link = self._do_pre(method, data)
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(link) as response:
                response_json = await response.json()
                return self._do_post(response_json, dataclass)

    @property
    def loop(self) -> asyncio.AbstractEventLoop:
        if self._loop is None:
            self._loop = asyncio.get_event_loop()
        return self._loop
