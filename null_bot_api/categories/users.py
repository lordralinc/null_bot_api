from null_bot_api import models
from null_bot_api.categories.base import BaseAPICategories


class UsersAPICategories(BaseAPICategories):

    def get_info(
            self,
            user_id: int,
    ) -> models.UsersGetInfo:
        """Метод позволяет получить общую информацию о пользователях ВКонтакте.
        :param user_id:     id пользователя информацию о котором нужно получить.
                            Передача короткого адреса (screen_name) невозможна!
        """
        return self.api.make_request(
            method='users.getInfo',
            data=dict(user_id=user_id),
            dataclass=models.UsersGetInfo
        )

    async def get_info_async(
            self,
            user_id: int
    ) -> models.UsersGetInfo:
        """Метод позволяет получить общую информацию о пользователях ВКонтакте.
        :param user_id:     id пользователя информацию о котором нужно получить.
                            Передача короткого адреса (screen_name) невозможна!
        """
        return await self.api.make_request_async(
            method='users.getInfo',
            data=dict(user_id=user_id),
            dataclass=models.UsersGetInfo
        )

    def get_stickers(
            self,
            user_id: int,
    ) -> models.UsersGetStickers:
        """Метод позволяет получить информацию о платных и бесплатных стикерах пользователях ВКонтакте.
        :param user_id:     id пользователя информацию о котором нужно получить.
                            Передача короткого адреса (screen_name) невозможна!
        """
        return self.api.make_request(
            method='users.getStickers',
            data=dict(user_id=user_id),
            dataclass=models.UsersGetStickers
        )

    async def get_stickers_async(
            self,
            user_id: int
    ) -> models.UsersGetStickers:
        """Метод позволяет получить информацию о платных и бесплатных стикерах пользователях ВКонтакте.
        :param user_id:     id пользователя информацию о котором нужно получить.
                            Передача короткого адреса (screen_name) невозможна!
        """
        return await self.api.make_request_async(
            method='users.getStickers',
            data=dict(user_id=user_id),
            dataclass=models.UsersGetStickers
        )

    def get_all(
            self,
            user_id: int,
    ) -> models.UsersGetAll:
        """Метод объединяет в себе выдачу методов `experts.get_info`, `testers.get_info`,
            `users.get_info` и `users.get_stickers`.
        :param user_id:     id пользователя информацию о котором нужно получить.
                            Передача короткого адреса (screen_name) невозможна!
        """
        return self.api.make_request(
            method='users.getAll',
            data=dict(user_id=user_id),
            dataclass=models.UsersGetAll
        )

    async def get_all_async(
            self,
            user_id: int
    ) -> models.UsersGetAll:
        """Метод объединяет в себе выдачу методов `experts.get_info`, `testers.get_info`,
            `users.get_info` и `users.get_stickers`.
        :param user_id:     id пользователя информацию о котором нужно получить.
                            Передача короткого адреса (screen_name) невозможна!
        """
        return await self.api.make_request_async(
            method='users.getAll',
            data=dict(user_id=user_id),
            dataclass=models.UsersGetAll
        )
