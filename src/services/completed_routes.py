from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.completed_routes import CompletedRoutes
from schemas.completed_routes import CompletedRouteCreate, CompletedRouteUpdate


class CompletedRouteService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_completed_route(self, completed_route_data: CompletedRouteCreate) -> CompletedRoutes:
        completed_route = CompletedRoutes(**completed_route_data.model_dump())
        self.session.add(completed_route)
        await self.session.commit()
        await self.session.refresh(completed_route)
        return completed_route

    async def get_completed_route(self, completed_route_id: int) -> CompletedRoutes | None:
        query = select(CompletedRoutes).where(CompletedRoutes.id == completed_route_id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def get_completed_routes(self, skip: int = 0, limit: int = 100) -> list[CompletedRoutes]:
        query = select(CompletedRoutes).offset(skip).limit(limit)
        result = await self.session.execute(query)
        return list(result.scalars().all())

    async def update_completed_route(
        self, completed_route_id: int, completed_route_data: CompletedRouteUpdate
    ) -> CompletedRoutes | None:
        query = select(CompletedRoutes).where(CompletedRoutes.id == completed_route_id)
        result = await self.session.execute(query)
        completed_route = result.scalar_one_or_none()
        
        if not completed_route:
            return None
            
        for key, value in completed_route_data.model_dump(exclude_unset=True).items():
            setattr(completed_route, key, value)
            
        await self.session.commit()
        await self.session.refresh(completed_route)
        return completed_route

    async def delete_completed_route(self, completed_route_id: int) -> bool:
        query = select(CompletedRoutes).where(CompletedRoutes.id == completed_route_id)
        result = await self.session.execute(query)
        completed_route = result.scalar_one_or_none()
        
        if not completed_route:
            return False
            
        await self.session.delete(completed_route)
        await self.session.commit()
        return True
