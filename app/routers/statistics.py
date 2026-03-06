from typing import Annotated
from fastapi import APIRouter, Depends, Query

from app.dependency import get_statistics_service
from app.services.statistics import StatisticsService
from app.schemas.statistics import StatisticsSchema

router = APIRouter(tags=["Statistics"])

# /habits/{habit_id}/stats?from=&to=
@router.get(path="/habits/{habit_id}/stats", response_model=StatisticsSchema)
def get_statistic(
		habit_id: int,
		date_from: Annotated[str | None, Query(alias="from")] = None,
		date_to: Annotated[str | None, Query(alias="to")] = None,
		statistics_service: StatisticsService = Depends(get_statistics_service)
):
	return statistics_service.get_statistics(habit_id, date_from, date_to)

