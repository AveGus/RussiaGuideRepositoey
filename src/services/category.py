from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.category import Category
from schemas.category import CategoryCreate, CategoryUpdate


class CategoryService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_category(self, category_data: CategoryCreate) -> Category:
        category = Category(**category_data.model_dump())
        self.session.add(category)
        await self.session.commit()
        await self.session.refresh(category)
        return category

    async def get_category(self, category_id: int) -> Category | None:
        query = select(Category).where(Category.id == category_id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def get_categories(self, skip: int = 0, limit: int = 100) -> list[Category]:
        query = select(Category).offset(skip).limit(limit)
        result = await self.session.execute(query)
        return list(result.scalars().all())

    async def update_category(self, category_id: int, category_data: CategoryUpdate) -> Category | None:
        query = select(Category).where(Category.id == category_id)
        result = await self.session.execute(query)
        category = result.scalar_one_or_none()
        
        if not category:
            return None
            
        for key, value in category_data.model_dump(exclude_unset=True).items():
            setattr(category, key, value)
            
        await self.session.commit()
        await self.session.refresh(category)
        return category

    async def delete_category(self, category_id: int) -> bool:
        query = select(Category).where(Category.id == category_id)
        result = await self.session.execute(query)
        category = result.scalar_one_or_none()
        
        if not category:
            return False
            
        await self.session.delete(category)
        await self.session.commit()
        return True
