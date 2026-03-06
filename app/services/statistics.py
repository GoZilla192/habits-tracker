from dataclasses import dataclass
import datetime

from app.exceptions import WrongDateFormat
from app.repository.habits import HabitsRepository
from app.repository.statistics import StatisticsRepository
from app.schemas.statistics import StatisticsSchema


@dataclass
class StatisticsService:
	statistic_repo: StatisticsRepository
	habit_repo: HabitsRepository
	
	async def get_statistics(
			self,
			habit_id: int,
			date_from: str | None,
			date_to: str | None
	) -> StatisticsSchema:
		if not date_from:
			date_from = await self.habit_repo.get_created_at_by_id(habit_id)
		else:
			date_from = await self._covert_string_to_date(date_str=date_from)
		
		if not date_to:
			date_to = datetime.datetime.now(datetime.timezone.utc).date()
		else:
			date_to = await self._covert_string_to_date(date_str=date_to)
		
		return StatisticsSchema.model_validate(
			await self.statistic_repo.get_statistic(habit_id, date_from, date_to)
		)
	
	def _covert_string_to_date(self, date_str: str) -> datetime.date:
		try:
			converted_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
		except ValueError:
			raise WrongDateFormat
		
		return converted_date