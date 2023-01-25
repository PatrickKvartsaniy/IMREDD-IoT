from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class ServiceSetting(BaseSettings):
    environment: str = "PROD"

    port: int = 8080
    host: str = "0.0.0.0"
    domain: str = "https://sbots-core.herokuapp.com"
    log_level: str = "INFO"

    db_host: str
    db_port: int = 5432
    db_name: str
    db_user: str
    db_password: str

    db_engine: str = "postgresql+asyncpg://"

    def database_uri(self) -> str:
        return self.db_engine + self.db_user + ":" + self.db_password + "@" + self.db_host + ":" + str(self.db_port) + "/" + self.db_name


config = ServiceSetting()
