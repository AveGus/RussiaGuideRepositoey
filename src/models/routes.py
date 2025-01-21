from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.city import City
from services.database import Base


class Routes(Base):
    __tablename__ = 'routes'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    city_id: Mapped[int] = mapped_column(ForeignKey('cities.id'))
    name: Mapped[str] = mapped_column(String(100))
    duration: Mapped[int] = mapped_column()
    description: Mapped[str] = mapped_column(String(1000))
    distance: Mapped[int] = mapped_column()
    updated_at: Mapped[str] = mapped_column(String(100))
    
    city: Mapped[City] = relationship(lazy='selectin')