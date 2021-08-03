import typing as ty

from pydantic import BaseModel, Field


class VKGetOlympMedal(BaseModel):
    id: int
    country_name: str
    logo: str

    bronze_str: str = Field(alias="bronze")
    silver_str: str = Field(alias="silver")
    gold_str: str = Field(alias="gold")

    @property
    def bronze(self) -> int:
        return int(self.bronze_str)

    @property
    def silver(self) -> int:
        return int(self.silver_str)

    @property
    def gold(self) -> int:
        return int(self.gold_str)


class VKGetOlymp(BaseModel):
    medals: ty.List[VKGetOlympMedal]
