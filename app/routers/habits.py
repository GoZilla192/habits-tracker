from fastapi import APIRouter, Depends

from app.dependency import get_habits_service
from app.services.habits import HabitsService
from app.schemas.habits import HabitsReadSchema, HabitsCreateSchema


router = APIRouter(tags=["habits"])

@router.post(path="/habit", response_model=HabitsReadSchema)
def create_habit(habit: HabitsCreateSchema, habits_service: HabitsService = Depends(get_habits_service)):
	return habits_service.create_habit(habit=habit)

@router.get(path="/habits", response_model=list[HabitsReadSchema])
def get_habits(habits_service: HabitsService = Depends(get_habits_service)):
	return habits_service.get_list_habits()
	