from null_bot_api import models
from null_bot_api.categories.base import BaseAPICategories


class VKAPICategories(BaseAPICategories):

    def get_olymp(
            self
    ) -> models.VKGetOlymp:
        """Метод возвращает информацию о медальном зачёте на олимпиаде
            Токио-2020 из соответствующей ленты (приложения) ВКонтакте.
        """
        return self.api.make_request(
            method='vk.getOlymp',
            data=dict(),
            dataclass=models.VKGetOlymp
        )

    async def get_olymp_async(
            self
    ) -> models.VKGetOlymp:
        """Метод возвращает информацию о медальном зачёте на олимпиаде
            Токио-2020 из соответствующей ленты (приложения) ВКонтакте.
        """
        return await self.api.make_request_async(
            method='vk.getOlymp',
            data=dict(),
            dataclass=models.VKGetOlymp
        )
