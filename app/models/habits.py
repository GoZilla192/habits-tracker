import datetime

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, func

from app.models.base import Base


class Habit(Base):
	__tablename__ = "habits"
	
	id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
	name: Mapped[str] = mapped_column(String(100), nullable=False)
	description: Mapped[str] = mapped_column(String(500), nullable=True)
	created_at: Mapped[datetime.date] = mapped_column(server_default=func.current_date())
	