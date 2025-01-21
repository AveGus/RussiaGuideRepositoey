from pydantic import BaseModel


class CompletedRouteBase(BaseModel):
    route_id: int


class CompletedRouteCreate(CompletedRouteBase):
    pass


class CompletedRouteUpdate(BaseModel):
    route_id: int | None = None


class CompletedRoute(CompletedRouteBase):
    id: int

    class Config:
        from_attributes = True
