import datetime
from pydantic import BaseModel, ConfigDict


class HabitsCreateSchema(BaseModel):
	name: str
	description: str | None = None


class HabitsReadSchema(BaseModel):
	id: int
	name: str
	description: str | None = None
	created_at: datetime.date
	
	model_config = ConfigDict(from_attributes=True) # for convert orm model to pydantic model
	
class HabitsUpdateSchema(BaseModel):
	name: str
	description: str | None = None
	