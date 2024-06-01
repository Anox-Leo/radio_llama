from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    fief_domain: str
    fief_client_id: str
    fief_client_secret: str

    model_config = SettingsConfigDict(env_file=".env")