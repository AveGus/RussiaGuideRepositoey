from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from services.database import get_async_session
from schemas.completed_routes import CompletedRoute, CompletedRouteCreate, CompletedRouteUpdate
from services.completed_routes import CompletedRouteService

router = APIRouter(prefix="/completed-routes", tags=["completed-routes"])


@router.post("/", response_model=CompletedRoute)
async def create_completed_route(
    completed_route_data: CompletedRouteCreate,
    session: AsyncSession = Depends(get_async_session)
):
    completed_route_service = CompletedRouteService(session)
    return await completed_route_service.create_completed_route(completed_route_data)


@router.get("/{completed_route_id}", response_model=CompletedRoute)
async def get_completed_route(
    completed_route_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    completed_route_service = CompletedRouteService(session)
    completed_route = await completed_route_service.get_completed_route(completed_route_id)
    if not completed_route:
        raise HTTPException(status_code=404, detail="Completed route not found")
    return completed_route


@router.get("/", response_model=list[CompletedRoute])
async def get_completed_routes(
    skip: int = 0,
    limit: int = 100,
    session: AsyncSession = Depends(get_async_session)
):
    completed_route_service = CompletedRouteService(session)
    return await completed_route_service.get_completed_routes(skip=skip, limit=limit)


@router.patch("/{completed_route_id}", response_model=CompletedRoute)
async def update_completed_route(
    completed_route_id: int,
    completed_route_data: CompletedRouteUpdate,
    session: AsyncSession = Depends(get_async_session)
):
    completed_route_service = CompletedRouteService(session)
    completed_route = await completed_route_service.update_completed_route(
        completed_route_id, completed_route_data
    )
    if not completed_route:
        raise HTTPException(status_code=404, detail="Completed route not found")
    return completed_route


@router.delete("/{completed_route_id}")
async def delete_completed_route(
    completed_route_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    completed_route_service = CompletedRouteService(session)
    if not await completed_route_service.delete_completed_route(completed_route_id):
        raise HTTPException(status_code=404, detail="Completed route not found")
    return {"ok": True}
