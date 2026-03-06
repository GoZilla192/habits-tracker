import datetime
from sqlalchemy import select, func, text

from app.repository.base import BaseRepository
from app.models.chekins import Checkin
from app.models.habits import Habit


class StatisticsRepository(BaseRepository):
	def get_statistic(
			self,
			habit_id: int,
			date_from: datetime.date,
			date_to: datetime.date
	) -> dict[[str, int | float | None]]:
		return {
			"percent_checkins": self._get_percent_checkins(habit_id, date_from, date_to),
			"max_streak": self._get_max_streak(habit_id, date_from, date_to),
			"curr_streak": self._get_curr_streak(habit_id, date_from, date_to),
		}
	
	
	def _get_percent_checkins(
			self,
			habit_id: int,
			date_from: datetime.date,
			date_to: datetime.date
	) -> float | None:
		query = (
			select(
				func.round(
					(
							func.count(Checkin.checkin_date) /
							(func.datediff(date_to, date_from) + 1)
					 ) * 100, 2)
			)
			.select_from(Checkin)
			.join(Habit, Habit.id == Checkin.habit_id, isouter=True)
			.where(
				Checkin.habit_id == habit_id,
				Checkin.checkin_date.between(date_from, date_to)
			)
		)
		
		return self._db_session.execute(query).scalar_one_or_none()
	
	
	def _get_max_streak(
			self,
			habit_id: id,
			date_from: datetime.date,
			date_to: datetime.date
	) -> int | None:
		row_number = func.row_number().over(
			partition_by=Checkin.habit_id,
			order_by=Checkin.checkin_date
		)
		
		grp = func.date_sub(
			Checkin.checkin_date,
			func.interval(row_number, "day")
		)
		
		subquery1 = (
			select(
				Checkin.habit_id,
				Checkin.checkin_date,
				func.date_sub(
					Checkin.checkin_date,
					text(
						"INTERVAL ROW_NUMBER() OVER "
						"(PARTITION BY habit_id ORDER BY checkin_date) DAY"
					)
				).label("grp"),
			)
			.where(
				Checkin.checkin_date.between(date_from, date_to)
			)
		).subquery()
		
		subquery2 = (
			select(
				subquery1.c.habit_id,
				func.count().label("streak")
			)
			.group_by(
				subquery1.c.habit_id,
				subquery1.c.grp
			)
		).subquery()
		
		query = (
			select(
				func.max(subquery2.c.streak)
			)
			.group_by(subquery2.c.habit_id)
		)
		
		return self._db_session.execute(query).scalar_one_or_none()
		
		
	def _get_curr_streak(
			self,
			habit_id: id,
			date_from: datetime.date,
			date_to: datetime.date
	) -> int | None:
		subquery = (
			select(
				Checkin.checkin_date,
				func.datediff(date_to, Checkin.checkin_date).label("diff"),
				(
						func.row_number()
						.over(order_by=Checkin.checkin_date.desc()) - 1
				).label("rn"),
			)
			.where(
				Checkin.habit_id == habit_id,
				Checkin.checkin_date.between(date_from, date_to)
			)
		).subquery()
		
		query = select(func.count()).where(subquery.c.diff == subquery.c.rn)
		
		return self._db_session.execute(query).scalar_one_or_none()