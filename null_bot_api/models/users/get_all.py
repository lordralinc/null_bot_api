from null_bot_api.models.experts.get_info import ExpertsGetInfo
from null_bot_api.models.testers.get_info import TestersGetInfo
from null_bot_api.models.users.get_stickers import UsersGetStickers
from null_bot_api.models.users.get_info import UsersGetInfo


class UsersGetAll(UsersGetInfo):
    stickers_info: UsersGetStickers
    experts_info: ExpertsGetInfo
    testers_info: TestersGetInfo
