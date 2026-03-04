from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
	sqlite_path_to_db: str = "habit_tracker.db" # for test
	
	MYSQL_DRIVER: str = "mysql+mysqldb"
	MYSQL_HOST: str
	MYSQL_PORT: int
	MYSQL_LOGIN: str
	MYSQL_PASSWORD: str
	MYSQL_DB: str
	
	model_config = SettingsConfigDict(env_file=".env")
	
	def get_sqlite_db_url_connection(self) -> str:
		return f"sqlite:///{self.sqlite_path_to_db}"
	
	def get_mysql_db_url_connection(self) -> str:
		return f"{self.MYSQL_DRIVER}://{self.MYSQL_LOGIN}:{self.MYSQL_PASSWORD}@{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DB}"
	
	@property
	def db_url(self) -> str:
		return self.get_mysql_db_url_connection()
	
	