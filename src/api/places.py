from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from services.database import get_async_session
from schemas.places import Place, PlaceCreate, PlaceUpdate
from services.places import PlaceService

router = APIRouter(prefix="/places", tags=["places"])


@router.post("/", response_model=Place)
async def create_place(
    place_data: PlaceCreate,
    session: AsyncSession = Depends(get_async_session)
):
    place_service = PlaceService(session)
    return await place_service.create_place(place_data)


@router.get("/{place_id}", response_model=Place)
async def get_place(
    place_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    place_service = PlaceService(session)
    place = await place_service.get_place(place_id)
    if not place:
        raise HTTPException(status_code=404, detail="Place not found")
    return place


@router.get("/", response_model=list[Place])
async def get_places(
    skip: int = 0,
    limit: int = 100,
    session: AsyncSession = Depends(get_async_session)
):
    place_service = PlaceService(session)
    return await place_service.get_places(skip=skip, limit=limit)


@router.get("/route/{route_id}", response_model=list[Place])
async def get_places_by_route(
    route_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    place_service = PlaceService(session)
    return await place_service.get_places_by_route(route_id)


@router.get("/category/{category_id}", response_model=list[Place])
async def get_places_by_category(
    category_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    place_service = PlaceService(session)
    return await place_service.get_places_by_category(category_id)


@router.put("/{place_id}", response_model=Place)
async def update_place(
    place_id: int,
    place_data: PlaceUpdate,
    session: AsyncSession = Depends(get_async_session)
):
    place_service = PlaceService(session)
    return await place_service.update_place(place_id, place_data)


@router.delete("/{place_id}")
async def delete_place(
    place_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    place_service = PlaceService(session)
    if not await place_service.delete_place(place_id):
        raise HTTPException(status_code=404, detail="Place not found")
    return {"ok": True}
