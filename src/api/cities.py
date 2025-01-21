from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from services.database import get_async_session
from schemas.city import City, CityCreate, CityUpdate
from services.city import CityService

router = APIRouter(prefix="/cities", tags=["cities"])


@router.post("/", response_model=City)
async def create_city(
    city_data: CityCreate,
    session: AsyncSession = Depends(get_async_session)
):
    city_service = CityService(session)
    return await city_service.create_city(city_data)


@router.get("/{city_id}", response_model=City)
async def get_city(
    city_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    city_service = CityService(session)
    city = await city_service.get_city(city_id)
    if not city:
        raise HTTPException(status_code=404, detail="City not found")
    return city


@router.get("/", response_model=list[City])
async def get_cities(
    skip: int = 0,
    limit: int = 100,
    session: AsyncSession = Depends(get_async_session)
):
    city_service = CityService(session)
    return await city_service.get_cities(skip=skip, limit=limit)


@router.patch("/{city_id}", response_model=City)
async def update_city(
    city_id: int,
    city_data: CityUpdate,
    session: AsyncSession = Depends(get_async_session)
):
    city_service = CityService(session)
    city = await city_service.update_city(city_id, city_data)
    if not city:
        raise HTTPException(status_code=404, detail="City not found")
    return city


@router.delete("/{city_id}")
async def delete_city(
    city_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    city_service = CityService(session)
    if not await city_service.delete_city(city_id):
        raise HTTPException(status_code=404, detail="City not found")
    return {"ok": True}
