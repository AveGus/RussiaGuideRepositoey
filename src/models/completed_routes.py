from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.routes import Routes
from services.database import Base


class CompletedRoutes(Base):
    __tablename__ = 'completed_routes'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    route_id: Mapped[int] = mapped_column(ForeignKey('routes.id'))
    #user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    
    route: Mapped[Routes] = relationship(lazy='selectin')