from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
	sqlite_path_to_db: str = "habit_tracker.db" # for test
	
	MYSQL_SYNC_DRIVER: str = "mysql+mysqldb"
	MYSQL_ASYNC_DRIVER: str = "mysql+aiomysql"
	MYSQL_HOST: str
	MYSQL_PORT: int
	MYSQL_LOGIN: str
	MYSQL_PASSWORD: str
	MYSQL_DB: str
	
	model_config = SettingsConfigDict(env_file=".env")
	
	def get_sqlite_sync_db_url_connection(self) -> str:
		return f"sqlite:///{self.sqlite_path_to_db}"
	
	def get_mysql_sync_db_url_connection(self) -> str:
		return f"{self.MYSQL_SYNC_DRIVER}://{self.MYSQL_LOGIN}:{self.MYSQL_PASSWORD}@{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DB}"
	
	@property
	def sync_db_url(self) -> str:
		return self.get_mysql_sync_db_url_connection()
	
	
	def get_mysql_async_db_url_connection(self) -> str:
		return f"{self.MYSQL_ASYNC_DRIVER}://{self.MYSQL_LOGIN}:{self.MYSQL_PASSWORD}@{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DB}"
	
	@property
	def async_db_url(self) -> str:
		return self.get_mysql_async_db_url_connection()
	
	