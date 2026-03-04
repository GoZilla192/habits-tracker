import datetime

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, func, ForeignKey

from app.models.base import Base


class Checkin(Base):
	__tablename__ = "checkins"
	
	id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
	habit_id: Mapped[int] = mapped_column(
		ForeignKey("habits.id", ondelete="CASCADE", onupdate="CASCADE")
	)
	checkin_date: Mapped[datetime.date] = mapped_column(server_default=func.now())
