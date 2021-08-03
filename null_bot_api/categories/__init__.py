from abc import abstractmethod
from typing import TYPE_CHECKING

from null_bot_api.abc import APICategoriesABC

from .experts import ExpertsAPICategories
from .testers import TestersAPICategories
from .users import UsersAPICategories
from .vk import VKAPICategories

if TYPE_CHECKING:
    from null_bot_api import NullBotAPI


class APICategories(APICategoriesABC):

    @property
    def experts(self) -> ExpertsAPICategories:
        return ExpertsAPICategories(self.api_instance)

    @property
    def testers(self) -> TestersAPICategories:
        return TestersAPICategories(self.api_instance)

    @property
    def users(self) -> UsersAPICategories:
        return UsersAPICategories(self.api_instance)

    @property
    def vk(self) -> VKAPICategories:
        return VKAPICategories(self.api_instance)

    @property
    @abstractmethod
    def api_instance(self) -> "NullBotAPI":
        pass
