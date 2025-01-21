from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from services.database import get_async_session
from schemas.category import Category, CategoryCreate, CategoryUpdate
from services.category import CategoryService

router = APIRouter(prefix="/categories", tags=["categories"])


@router.post("/", response_model=Category)
async def create_category(
    category_data: CategoryCreate,
    session: AsyncSession = Depends(get_async_session)
):
    category_service = CategoryService(session)
    return await category_service.create_category(category_data)


@router.get("/{category_id}", response_model=Category)
async def get_category(
    category_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    category_service = CategoryService(session)
    category = await category_service.get_category(category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.get("/", response_model=list[Category])
async def get_categories(
    skip: int = 0,
    limit: int = 100,
    session: AsyncSession = Depends(get_async_session)
):
    category_service = CategoryService(session)
    return await category_service.get_categories(skip=skip, limit=limit)


@router.patch("/{category_id}", response_model=Category)
async def update_category(
    category_id: int,
    category_data: CategoryUpdate,
    session: AsyncSession = Depends(get_async_session)
):
    category_service = CategoryService(session)
    category = await category_service.update_category(category_id, category_data)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.delete("/{category_id}")
async def delete_category(
    category_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    category_service = CategoryService(session)
    if not await category_service.delete_category(category_id):
        raise HTTPException(status_code=404, detail="Category not found")
    return {"ok": True}
