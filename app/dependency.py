from fastapi import Depends

from app.database.accessor import get_db_session
from app.repository.habits import HabitsRepository
from app.services.habits import HabitsService


def get_habits_repository(db_session = Depends(get_db_session)):
	return HabitsRepository(db_session=db_session)

def get_habits_service(habit_repo = Depends(get_habits_repository)):
	return HabitsService(habit_repo=habit_repo)
