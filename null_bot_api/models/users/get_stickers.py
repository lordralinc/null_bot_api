from pydantic import BaseModel


class UsersGetStickers(BaseModel):
    all: int
    paid: int
    time: float
