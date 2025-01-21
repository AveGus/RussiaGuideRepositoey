from pydantic import BaseModel


class PlaceBase(BaseModel):
    name: str
    description: str
    latitude: str
    longitude: str
    opening_hours: str
    route_id: int
    category_id: int


class PlaceCreate(PlaceBase):
    pass


class PlaceUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    latitude: str | None = None
    longitude: str | None = None
    opening_hours: str | None = None
    route_id: int | None = None
    category_id: int | None = None
    photos: list[str] | None = None


class Place(PlaceBase):
    id: int

    class Config:
        from_attributes = True
