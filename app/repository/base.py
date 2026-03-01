from sqlalchemy.orm import Session

class BaseRepository:
	def __init__(self, db_session: Session):
		self._db_session: Session = db_session
		