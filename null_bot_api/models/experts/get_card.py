import typing as ty

from pydantic import BaseModel


class ExpertsGetCardWeeklyGoal(BaseModel):
    id: str
    title: str
    current_value: int
    goal: int


class ExpertsGetCardAchievements(BaseModel):
    avatar: str
    description: str
    title: str


class ExpertsGetCard(BaseModel):
    user_id: int

    first_name: str
    last_name: str
    avatar: str
    balance: int
    points: float
    date_invite: int
    shop_link: str
    categories: ty.List[str]

    achievements: ty.List[ExpertsGetCardAchievements]
    weekly_goal: ExpertsGetCardWeeklyGoal
