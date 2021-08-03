from null_bot_api import models
from null_bot_api.categories.base import BaseAPICategories


class TestersAPICategories(BaseAPICategories):

    def get_info(
            self,
            user_id: int,
    ) -> models.TestersGetInfo:
        """Метод позволяет получить информацию о пользователях, состоящих в программе VK Testers.
        :param user_id:     id пользователя информацию о котором нужно получить.
                            Передача короткого адреса (screen_name) невозможна!
        """
        return self.api.make_request(
            method='testers.getInfo',
            data=dict(user_id=user_id),
            dataclass=models.TestersGetInfo
        )

    async def get_info_async(
            self,
            user_id: int
    ) -> models.TestersGetInfo:
        """Метод позволяет получить информацию о пользователях, состоящих в программе VK Testers.
        :param user_id:     id пользователя информацию о котором нужно получить.
                            Передача короткого адреса (screen_name) невозможна!
        """
        return await self.api.make_request_async(
            method='testers.getInfo',
            data=dict(user_id=user_id),
            dataclass=models.TestersGetInfo
        )
