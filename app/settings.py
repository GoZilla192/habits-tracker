from pydantic_settings import BaseSettings


class Settings(BaseSettings):
	sqlite_path_to_db: str = "habit_tracker.db"
	
	@property
	def sqlite_db_url(self):
		return f"sqlite:///{self.sqlite_path_to_db}"