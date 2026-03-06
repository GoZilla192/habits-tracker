from fastapi import APIRouter, Depends, status, HTTPException

from app.dependency import get_checkins_service
from app.exceptions import CheckinAlreadyExists, WrongDateFormat
from app.services.checkins import CheckinsService

router = APIRouter(tags=["Checkins"])


@router.post(path="/habits/{habit_id}/checkins", status_code=status.HTTP_201_CREATED)
def set_checkin(habit_id: int, checkins_service: CheckinsService = Depends(get_checkins_service)):
	try:
		checkins_service.set_checkin(habit_id=habit_id)
	except CheckinAlreadyExists as e:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Checkin by this habit already exists"
		)
	

@router.delete(path="/habits/{habit_id}/checkins", status_code=status.HTTP_204_NO_CONTENT)
def delete_checkin(
		habit_id: int,
		date: str,
		checkins_service: CheckinsService = Depends(get_checkins_service)
):
	try:
		checkins_service.delete_checkin(habit_id=habit_id, date=date)
	except WrongDateFormat:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Wrong date format. "
			       "Expected date format: 'yyyy-mm-dd', "
			       "Examples: '2026-03-05', '2026-12-01' "
		)