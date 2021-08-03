import typing as ty
from pydantic import BaseModel


class TestersGetInfoBugReportProduct(BaseModel):
    id: int
    name: str


class TestersGetInfoBugReportReproduces(BaseModel):
    count: int


class TestersGetInfoBugReportStatus(BaseModel):
    id: int
    name: str


class TestersGetInfoBugReportTag(BaseModel):
    id: int
    name: str


class TestersGetInfoBugReport(BaseModel):
    id: int
    owner_id: int
    title: str

    created: int
    updated: int

    comments_count: ty.Optional[int]

    product: TestersGetInfoBugReportProduct
    reproduces: TestersGetInfoBugReportReproduces
    status: TestersGetInfoBugReportTag
    tags: ty.List[TestersGetInfoBugReportTag]


class TestersGetInfoBugReports(BaseModel):
    count: int
    items: ty.List[TestersGetInfoBugReport]
    next_from: ty.Optional[int] = None


class TestersGetInfoUserInfo(BaseModel):
    id: int
    first_name: str
    last_name: str
    is_closed: bool
    reports_count: int
    top_position: int
    status_text: str


class TestersGetInfoProducts(BaseModel):
    available_products_count: int
    secret_products_count: int
    secret_reports_count: int
    uncounted_reports_count: int
    unshown_reports_count: int


class TestersGetInfo(BaseModel):
    is_tester: bool

    products: ty.Optional[TestersGetInfoProducts]
    user_info: ty.Optional[TestersGetInfoUserInfo]
    bugreports: ty.Optional[TestersGetInfoBugReports]
