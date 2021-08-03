import typing as ty

from null_bot_api import models
from null_bot_api.categories.base import BaseAPICategories


class ExpertsAPICategories(BaseAPICategories):

    def get_info(
            self,
            user_id: ty.Optional[ty.Union[str, int]] = None,
            user_ids: ty.Optional[ty.List[ty.Union[str, int]]] = None
    ) -> models.ExpertsGetInfo:
        """Метод позволяет получить информацию о пользователях, состоящих в Экспертах ВКонтакте.
        :param user_id:     обязательный;
                            id пользователя или его короткое имя (screen_name), информацию о котором нужно получить.
                            Например: 123 или ryzhov.andrey.
                            Предпочтительнее передавать id пользователя (так работает быстрее).

        :param user_ids:    обязательный, если не указан user_id;
                            id пользователей или их короткие имена, разделённые запятыми,
                            о которых нужно получить информацию.
                            Максимальное количество: 100.
                            Например: 123,andrew,456.
        """
        return self.api.make_request(
            method='experts.getInfo',
            data=dict(user_id=user_id, user_ids=user_ids),
            dataclass=models.ExpertsGetInfo
        )

    async def get_info_async(
            self,
            user_id: ty.Optional[ty.Union[str, int]] = None,
            user_ids: ty.Optional[ty.List[ty.Union[str, int]]] = None
    ) -> models.ExpertsGetInfo:
        """Метод позволяет получить информацию о пользователях, состоящих в Экспертах ВКонтакте.
        :param user_id:     обязательный;
                            id пользователя или его короткое имя (screen_name), информацию о котором нужно получить.
                            Например: 123 или ryzhov.andrey.
                            Предпочтительнее передавать id пользователя (так работает быстрее).

        :param user_ids:    обязательный, если не указан user_id;
                            id пользователей или их короткие имена, разделённые запятыми,
                            о которых нужно получить информацию.
                            Максимальное количество: 100.
                            Например: 123,andrew,456.
        """
        return await self.api.make_request_async(
            method='experts.getInfo',
            data=dict(user_id=user_id, user_ids=user_ids),
            dataclass=models.ExpertsGetInfo
        )

    def get_card(
            self,
            access_token: str
    ) -> models.ExpertsGetCard:
        """Метод позволяет получить карточку Эксперта ВКонтакте текущего пользователя.
        :param access_token:    токен пользователя, карточку которого нужно получить.
                                Например: 8f8efw9fj89h7h8fwrg9hug8fywe9h80rj4f3rneu9.

                                Подходят токены только от VK Me и VK для Android, никаких прав не нужно.
                                Получить токен можно тут: https://vkhost.github.io.
        """
        return self.api.make_request(
            method='experts.getCard',
            data=dict(access_token=access_token),
            dataclass=models.ExpertsGetCard
        )

    async def get_card_async(
            self,
            access_token: str
    ) -> models.ExpertsGetCard:
        """Метод позволяет получить карточку Эксперта ВКонтакте текущего пользователя.
        :param access_token:    токен пользователя, карточку которого нужно получить.
                                Например: 8f8efw9fj89h7h8fwrg9hug8fywe9h80rj4f3rneu9.

                                Подходят токены только от VK Me и VK для Android, никаких прав не нужно.
                                Получить токен можно тут: https://vkhost.github.io.
        """
        return await self.api.make_request_async(
            method='experts.getCard',
            data=dict(access_token=access_token),
            dataclass=models.ExpertsGetCard
        )
