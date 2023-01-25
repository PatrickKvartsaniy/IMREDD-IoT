from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class ServiceSetting(BaseSettings):
    environment: str = "PROD"

    port: int = 8080
    host: str = "0.0.0.0"
    domain: str = "https://sbots-core.herokuapp.com"
    log_level: str = "INFO"

    db_host: str = "dpg-cf8jgkpmbjss4md9k830-a"
    db_port: int = 5432
    db_name: str = "imredd"
    db_user: str = "imredd"
    db_password: str = "LVFfzkZ4kCpNQEwJtY1Mpf4wIPXwRRxg"

    db_engine: str = "postgresql+asyncpg://"

    telegram_token: str = "5987475158:AAEnnggV4A_ty70dLzxf7SOEzGLkja9Kjl0"

    def database_uri(self) -> str:
        return self.db_engine + self.db_user + ":" + self.db_password + "@" + self.db_host + ":" + str(self.db_port) + "/" + self.db_name


config = ServiceSetting()
