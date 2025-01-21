from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from services.database import Base

class City(Base):
    __tablename__ = "cities"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(1000))
    latitude:  Mapped[str] = mapped_column(String(100), nullable=True)
    longitude:  Mapped[str] = mapped_column(String(100), nullable=True)
