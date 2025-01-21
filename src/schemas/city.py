from pydantic import BaseModel


class CityBase(BaseModel):
    name: str
    description: str
    latitude: str | None = None
    longitude: str | None = None


class CityCreate(CityBase):
    pass


class CityUpdate(CityBase):
    name: str | None = None
    description: str | None = None


class City(CityBase):
    id: int

    class Config:
        from_attributes = True
