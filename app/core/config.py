from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "AI Dev Assistant"
    debug: bool = False


settings = Settings()
