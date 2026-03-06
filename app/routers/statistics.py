from typing import Annotated, Union
from fastapi import APIRouter, Depends, Query, HTTPException, status

from app.dependency import get_statistics_service
from app.exceptions import WrongDateFormat
from app.services.statistics import StatisticsService
from app.schemas.statistics import StatisticsSchema

router = APIRouter(tags=["Statistics"])

@router.get(path="/habits/{habit_id}/stats", response_model=StatisticsSchema)
def get_statistic(
		habit_id: int,
		date_from: Annotated[str | None, Query(alias="from")] = None,
		date_to: Annotated[str | None, Query(alias="to")] = None,
		statistics_service: StatisticsService = Depends(get_statistics_service)
):
	try:
		return statistics_service.get_statistics(habit_id, date_from, date_to)
	except WrongDateFormat:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Wrong date format. "
			       "Expected date format: 'yyyy-mm-dd', "
			       "Examples: '2026-03-05', '2026-12-01' "
		)
