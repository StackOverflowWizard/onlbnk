from functools import cache

from pydantic import Field
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    project_name: str = Field(validation_alias="PROJECT_NAME", default="gateway")
    project_host: str = Field(validation_alias="GATEWAY_APP_HOST", default="0.0.0.0")
    project_port: int = Field(validation_alias="GATEWAY_APP_PORT", default=9000)
    is_debug: bool = Field(validation_alias="DEBUG", default=True)


class Settings(BaseSettings):
    app: AppSettings = Field(default_factory=AppSettings)


@cache
def get_settings() -> Settings:
    return Settings()
