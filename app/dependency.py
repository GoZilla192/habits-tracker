from fastapi import Depends

from app.database.accessor import get_db_session
from app.repository.checkins import CheckinsRepository
from app.repository.habits import HabitsRepository
from app.services.habits import HabitsService
from app.services.checkins import CheckinsService


def get_habits_repository(db_session = Depends(get_db_session)):
	return HabitsRepository(db_session=db_session)


def get_checkins_repository(db_session = Depends(get_db_session)):
	return CheckinsRepository(db_session=db_session)


def get_checkins_service(checkin_repo = Depends(get_checkins_repository)):
	return CheckinsService(checkin_repo=checkin_repo)


def get_habits_service(habit_repo = Depends(get_habits_repository)):
	return HabitsService(habit_repo=habit_repo)

