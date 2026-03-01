from dataclasses import dataclass

from app.repository.habits import HabitsRepository
from app.schemas.habits import HabitsCreateSchema, HabitsReadSchema


@dataclass
class HabitsService:
	habit_repo: HabitsRepository
	
	def create_habit(self, habit: HabitsCreateSchema) -> HabitsReadSchema:
		habit_model = self.habit_repo.create_habit(habit.name, habit.description)
		return HabitsReadSchema(
			id=habit_model.id,
			name=habit_model.name,
			description=habit_model.description,
			created_at=habit_model.created_at
		)
	