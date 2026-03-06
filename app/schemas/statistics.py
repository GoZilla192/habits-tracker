from pydantic import BaseModel


class StatisticsSchema(BaseModel):
	percent_checkins: float | None
	max_streak: int | None
	curr_streak: int | None
	