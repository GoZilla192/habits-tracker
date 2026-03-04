from dataclasses import dataclass

from app.repository.habits import HabitsRepository
from app.schemas.habits import HabitsCreateSchema, HabitsReadSchema, HabitsUpdateSchema


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
	
	def get_list_habits(self) -> list[HabitsReadSchema]:
		return [
			HabitsReadSchema.model_validate(habit_model) for habit_model in self.habit_repo.get_habits()
		]

	def update_habit(self, habit_id: int, body: HabitsUpdateSchema) -> HabitsReadSchema:
		return self.habit_repo.update_habit(
			habit_id=habit_id,
			new_habit_name=body.name,
			new_description=body.description
		)