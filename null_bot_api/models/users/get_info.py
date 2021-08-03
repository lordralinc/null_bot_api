import typing as ty
from pydantic import BaseModel, Field
from datetime import datetime


class UsersGetInfo(BaseModel):
    domain: ty.Optional[str]
    first_name: ty.Optional[str]
    last_name: ty.Optional[str]
    name: ty.Optional[str]
    nick: ty.Optional[str]
    status: ty.Optional[str]

    subscribers_count: ty.Optional[int]
    subscribed_to_count: ty.Optional[int]
    gender: ty.Optional[str]
    birthday: ty.Optional[str]
    bio: ty.Optional[str]

    profile_state_str: ty.Optional[str] = Field(alias='profile_state')
    public_access_str: ty.Optional[str] = Field(alias='public_access')

    created_str: ty.Optional[str] = Field(alias='created')
    modified_str: ty.Optional[str] = Field(alias='modified')
    last_online_str: ty.Optional[str] = Field(alias='last_online')

    @property
    def profile_state(self) -> ty.Optional[bool]:
        return self.profile_state_str == 'active' if self.profile_state_str else None

    @property
    def public_access(self) -> ty.Optional[bool]:
        return self.public_access_str == 'allowed' if self.public_access_str else None

    @property
    def created(self) -> ty.Optional[datetime]:
        if not self.created_str:
            return None
        try:
            return datetime.strptime(self.created_str, "%d.%m.%Y, %H:%M:%S")
        except:
            return None

    @property
    def modified(self) -> ty.Optional[datetime]:
        if not self.modified_str:
            return None
        try:
            return datetime.strptime(self.modified_str, "%d.%m.%Y, %H:%M:%S")
        except:
            return None

    @property
    def last_online(self) -> ty.Optional[datetime]:
        if not self.last_online_str:
            return None
        try:
            return datetime.strptime(self.last_online_str, "%d.%m.%Y, %H:%M:%S")
        except:
            return None
