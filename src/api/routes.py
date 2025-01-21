from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from services.database import get_async_session
from schemas.routes import Route, RouteCreate, RouteUpdate
from services.routes import RouteService

router = APIRouter(prefix="/routes", tags=["routes"])


@router.post("/", response_model=Route)
async def create_route(
    route_data: RouteCreate,
    session: AsyncSession = Depends(get_async_session)
):
    route_service = RouteService(session)
    return await route_service.create_route(route_data)


@router.get("/{route_id}", response_model=Route)
async def get_route(
    route_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    route_service = RouteService(session)
    route = await route_service.get_route(route_id)
    if not route:
        raise HTTPException(status_code=404, detail="Route not found")
    return route


@router.get("/", response_model=list[Route])
async def get_routes(
    skip: int = 0,
    limit: int = 100,
    session: AsyncSession = Depends(get_async_session)
):
    route_service = RouteService(session)
    return await route_service.get_routes(skip=skip, limit=limit)


@router.patch("/{route_id}", response_model=Route)
async def update_route(
    route_id: int,
    route_data: RouteUpdate,
    session: AsyncSession = Depends(get_async_session)
):
    route_service = RouteService(session)
    route = await route_service.update_route(route_id, route_data)
    if not route:
        raise HTTPException(status_code=404, detail="Route not found")
    return route


@router.delete("/{route_id}")
async def delete_route(
    route_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    route_service = RouteService(session)
    if not await route_service.delete_route(route_id):
        raise HTTPException(status_code=404, detail="Route not found")
    return {"ok": True}
