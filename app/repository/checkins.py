import datetime
from sqlalchemy import select, delete

from app.repository.base import BaseRepository
from app.models.chekins import Checkin
from app.exceptions import CheckinAlreadyExists


class CheckinsRepository(BaseRepository):
	def set_checkin(self, habit_id: int) -> None:
		if self._is_checkin_exist(habit_id=habit_id):
			raise CheckinAlreadyExists
		
		checkin = Checkin(habit_id=habit_id)
		self._db_session.add(checkin)
		self._db_session.commit()
	
	
	def delete_checkin(self, habit_id: int, date: datetime.date) -> None:
		stmt = delete(Checkin).where(
			(Checkin.habit_id == habit_id) &
			(Checkin.checkin_date == datetime.datetime.now(datetime.UTC).date())
		)
		self._db_session.execute(stmt)
		self._db_session.commit()
	
	
	def _is_checkin_exist(self, habit_id: int) -> bool:
		stmt = select(Checkin).where(
			(Checkin.habit_id == habit_id) &
			(Checkin.checkin_date == datetime.datetime.now(datetime.UTC).date())
		)
		checkins = self._db_session.execute(stmt)
		return bool(checkins.scalars().first())
		