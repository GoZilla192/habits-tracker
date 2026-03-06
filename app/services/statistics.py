from dataclasses import dataclass
import datetime

from app.repository.habits import HabitsRepository
from app.repository.statistics import StatisticsRepository
from app.schemas.statistics import StatisticsSchema


@dataclass
class StatisticsService:
	statistic_repo: StatisticsRepository
	habit_repo: HabitsRepository
	
	def get_statistics(
			self,
			habit_id: int,
			date_from: str | None,
			date_to: str | None
	) -> StatisticsSchema:
		if not date_from:
			date_from = self.habit_repo.get_created_at_by_id(habit_id)
		else:
			date_from = datetime.datetime.strptime(date_from, "%Y-%m-%d")
		
		if not date_to:
			date_to = datetime.datetime.now(datetime.timezone.utc).date()
		else:
			date_to = datetime.datetime.strptime(date_to, "%Y-%m-%d")
		
		return StatisticsSchema.model_validate(
			self.statistic_repo.get_statistic(habit_id, date_from, date_to)
		)