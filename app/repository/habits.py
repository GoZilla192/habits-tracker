import datetime
from sqlalchemy import select, update

from app.repository.base import BaseRepository
from app.models.habits import Habit


class HabitsRepository(BaseRepository):
	async def create_habit(self, habit_name: str, description: str | None) -> Habit:
		habit = Habit(name=habit_name, description=description)
		await self._db_session.add(habit)
		await self._db_session.commit()
		return habit
	
	
	async def update_habit(
			self, habit_id: int, new_habit_name: str, new_description: str | None
	) -> Habit | None:
		stmt = update(Habit).where(Habit.id == habit_id).values(
			name=new_habit_name, description=new_description
		)
		
		await self._db_session.execute(stmt)
		await self._db_session.commit()
		return await self.get_habit_by_id(habit_id)
	
	
	async def get_habit_by_id(self, habit_id: int) -> Habit | None:
		return (await self._db_session.execute(
			select(Habit).where(Habit.id == habit_id)
		)).scalar_one_or_none()
	
	
	async def get_habits(self) -> list[Habit]:
		return (await self._db_session.execute(select(Habit))).scalars().all()
	
	
	async def get_created_at_by_id(self, habit_id: id) -> datetime.date:
		stmt = select(Habit.created_at).where(Habit.id == habit_id)
		return (await self._db_session.execute(stmt)).scalar()
	