import datetime
from pydantic import BaseModel, ConfigDict


class HabitsCreateSchema(BaseModel):
	name: str
	description: str | None


class HabitsReadSchema(BaseModel):
	id: int
	name: str
	description: str | None
	created_at: datetime.date | None
	
	model_config = ConfigDict(from_attributes=True) # for convert orm model to pydantic model
	
class HabitsUpdateSchema(BaseModel):
	id: int
	name: str
	description: str | None
	