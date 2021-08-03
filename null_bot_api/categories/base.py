from typing import TYPE_CHECKING

from null_bot_api.abc import BaseAPICategoriesABC

if TYPE_CHECKING:
    from null_bot_api import NullBotAPI


class BaseAPICategories(BaseAPICategoriesABC):

    def __init__(self, api: "NullBotAPI"):
        self.api = api
