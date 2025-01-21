from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.city import City
from schemas.city import CityCreate, CityUpdate


class CityService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_city(self, city_data: CityCreate) -> City:
        city = City(**city_data.model_dump())
        self.session.add(city)
        await self.session.commit()
        await self.session.refresh(city)
        return city

    async def get_city(self, city_id: int) -> City | None:
        query = select(City).where(City.id == city_id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def get_cities(self, skip: int = 0, limit: int = 100) -> list[City]:
        query = select(City).offset(skip).limit(limit)
        result = await self.session.execute(query)
        return list(result.scalars().all())

    async def update_city(self, city_id: int, city_data: CityUpdate) -> City | None:
        query = select(City).where(City.id == city_id)
        result = await self.session.execute(query)
        city = result.scalar_one_or_none()
        
        if not city:
            return None
            
        for key, value in city_data.model_dump(exclude_unset=True).items():
            setattr(city, key, value)
            
        await self.session.commit()
        await self.session.refresh(city)
        return city

    async def delete_city(self, city_id: int) -> bool:
        query = select(City).where(City.id == city_id)
        result = await self.session.execute(query)
        city = result.scalar_one_or_none()
        
        if not city:
            return False
            
        await self.session.delete(city)
        await self.session.commit()
        return True
