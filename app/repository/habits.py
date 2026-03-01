from sqlalchemy import select, update

from app.repository.base import BaseRepository
from app.models.habits import Habit

class HabitsRepository(BaseRepository):
	def create_habit(self, habit_name: str, description: str | None) -> Habit:
		habit = Habit(name=habit_name, description=description)
		self._db_session.add(habit)
		self._db_session.commit()
		return habit
	
	def update_habit(
			self, habit_id: int, new_habit_name: str, new_description: str | None
	) -> Habit | None:
		stmt = update(Habit).where(Habit.id == habit_id).values(
			name=habit_name, description=new_description
		).returning(Habit.id)
		
		habit_id = self._db_session.execute(stmt)
		self._db_session.commit()
		return self.get_habit_by_id(habit_id)
	
	def get_habit_by_id(self, habit_id: int) -> Habit | None:
		return self._db_session.execute(
			select(Habit).where(Habit.id == habit_id)
		).scalar_one_or_none()
	
	def get_habits(self) -> list[Habit]:
		return self._db_session.execute(select(Habit)).scalars().all()
	