import typing as ty

from pydantic import BaseModel


class ExpertsGetInfoItemInfo(BaseModel):
    user_id: int
    position: ty.Optional[int] = None
    topic_name: ty.Optional[str] = None
    actions_count: ty.Optional[int] = None


class ExpertsGetInfoItem(BaseModel):
    is_expert: bool
    info: ExpertsGetInfoItemInfo


class ExpertsGetInfo(BaseModel):
    count: int
    items: ty.List[ExpertsGetInfoItem]
