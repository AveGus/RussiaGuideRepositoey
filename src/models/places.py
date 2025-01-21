from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.routes import Routes
from models.category import Category
from services.database import Base


class Places(Base):
    __tablename__ = 'places'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    route_id: Mapped[int] = mapped_column(ForeignKey('routes.id'))
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(1000))
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    latitude: Mapped[str] = mapped_column(String(100))
    longitude: Mapped[str] = mapped_column(String(100))
    opening_hours: Mapped[str] = mapped_column(String(100))
    
    route: Mapped[Routes] = relationship(lazy='selectin')
    category: Mapped[Category] = relationship(lazy='selectin')
