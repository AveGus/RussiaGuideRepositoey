from pydantic import BaseModel


class RouteBase(BaseModel):
    name: str
    duration: int
    description: str
    distance: int
    updated_at: str
    city_id: int


class RouteCreate(RouteBase):
    pass


class RouteUpdate(BaseModel):
    name: str | None = None
    duration: int | None = None
    description: str | None = None
    distance: int | None = None
    updated_at: str | None = None
    city_id: int | None = None


class Route(RouteBase):
    id: int

    class Config:
        from_attributes = True
