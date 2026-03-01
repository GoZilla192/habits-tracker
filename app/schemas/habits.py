import datetime
from pydantic import BaseModel


class HabitsCreateSchema(BaseModel):
	name: str
	description: str | None


class HabitsReadSchema(BaseModel):
	id: int
	name: str
	description: str | None
	created_at: datetime.date
	
	
class HabitsUpdateSchema(BaseModel):
	id: int
	name: str
	description: str | None
	