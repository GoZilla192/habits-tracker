from fastapi import Depends

from app.database.accessor import get_db_session
from app.repository.checkins import CheckinsRepository
from app.repository.habits import HabitsRepository
from app.repository.statistics import StatisticsRepository
from app.services.habits import HabitsService
from app.services.checkins import CheckinsService
from app.services.statistics import StatisticsService


def get_habits_repository(db_session = Depends(get_db_session)):
	return HabitsRepository(db_session=db_session)


def get_checkins_repository(db_session = Depends(get_db_session)):
	return CheckinsRepository(db_session=db_session)


def get_statistics_repository(db_session = Depends(get_db_session)):
	return StatisticsRepository(db_session=db_session)


def get_statistics_service(
		statistic_repo = Depends(get_statistics_repository),
		habit_repo = Depends(get_habits_repository)
):
	return StatisticsService(statistic_repo=statistic_repo, habit_repo=habit_repo)


def get_checkins_service(checkin_repo = Depends(get_checkins_repository)):
	return CheckinsService(checkin_repo=checkin_repo)


def get_habits_service(habit_repo = Depends(get_habits_repository)):
	return HabitsService(habit_repo=habit_repo)

