from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.routes import Routes
from schemas.routes import RouteCreate, RouteUpdate


class RouteService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_route(self, route_data: RouteCreate) -> Routes:
        route = Routes(**route_data.model_dump())
        self.session.add(route)
        await self.session.commit()
        await self.session.refresh(route)
        return route

    async def get_route(self, route_id: int) -> Routes | None:
        query = select(Routes).where(Routes.id == route_id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def get_routes(self, skip: int = 0, limit: int = 100) -> list[Routes]:
        query = select(Routes).offset(skip).limit(limit)
        result = await self.session.execute(query)
        return list(result.scalars().all())

    async def update_route(self, route_id: int, route_data: RouteUpdate) -> Routes | None:
        query = select(Routes).where(Routes.id == route_id)
        result = await self.session.execute(query)
        route = result.scalar_one_or_none()
        
        if not route:
            return None
            
        for key, value in route_data.model_dump(exclude_unset=True).items():
            setattr(route, key, value)
            
        await self.session.commit()
        await self.session.refresh(route)
        return route

    async def delete_route(self, route_id: int) -> bool:
        query = select(Routes).where(Routes.id == route_id)
        result = await self.session.execute(query)
        route = result.scalar_one_or_none()
        
        if not route:
            return False
            
        await self.session.delete(route)
        await self.session.commit()
        return True
