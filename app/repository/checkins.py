import datetime
from sqlalchemy import select, delete

from app.repository.base import BaseRepository
from app.models.chekins import Checkin
from app.exceptions import CheckinAlreadyExists


class CheckinsRepository(BaseRepository):
	async def set_checkin(self, habit_id: int) -> None:
		if await self._is_checkin_exist(habit_id=habit_id):
			raise CheckinAlreadyExists
		
		checkin = Checkin(habit_id=habit_id)
		await self._db_session.add(checkin)
		await self._db_session.commit()
	
	
	async def delete_checkin(self, habit_id: int, date: datetime.date) -> None:
		stmt = delete(Checkin).where(
			(Checkin.habit_id == habit_id) &
			(Checkin.checkin_date == datetime.datetime.now(datetime.UTC).date())
		)
		await self._db_session.execute(stmt)
		await self._db_session.commit()
	
	
	async def _is_checkin_exist(self, habit_id: int) -> bool:
		stmt = select(Checkin).where(
			(Checkin.habit_id == habit_id) &
			(Checkin.checkin_date == datetime.datetime.now(datetime.UTC).date())
		)
		checkins = await self._db_session.execute(stmt)
		return bool(checkins.scalars().first())
		