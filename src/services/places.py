from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.places import Places
from schemas.places import PlaceCreate, PlaceUpdate


class PlaceService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_place(self, place_data: PlaceCreate) -> Places:
        place = Places(**place_data.model_dump())
        self.session.add(place)
        await self.session.commit()
        await self.session.refresh(place)
        return place

    async def get_place(self, place_id: int) -> Places | None:
        query = select(Places).where(Places.id == place_id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def get_places(self, skip: int = 0, limit: int = 100) -> list[Places]:
        query = select(Places).offset(skip).limit(limit)
        result = await self.session.execute(query)
        return list(result.scalars().all())

    async def get_places_by_route(self, route_id: int) -> list[Places]:
        query = select(Places).where(Places.route_id == route_id)
        result = await self.session.execute(query)
        return list(result.scalars().all())

    async def get_places_by_category(self, category_id: int) -> list[Places]:
        query = select(Places).where(Places.category_id == category_id)
        result = await self.session.execute(query)
        return list(result.scalars().all())

    async def update_place(self, place_id: int, place_data: PlaceUpdate) -> Places | None:
        query = select(Places).where(Places.id == place_id)
        result = await self.session.execute(query)
        place = result.scalar_one_or_none()
        
        if not place:
            return None
            
        for key, value in place_data.model_dump(exclude_unset=True).items():
            setattr(place, key, value)
            
        await self.session.commit()
        await self.session.refresh(place)
        return place

    async def delete_place(self, place_id: int) -> bool:
        query = select(Places).where(Places.id == place_id)
        result = await self.session.execute(query)
        place = result.scalar_one_or_none()
        
        if not place:
            return False
            
        await self.session.delete(place)
        await self.session.commit()
        return True
