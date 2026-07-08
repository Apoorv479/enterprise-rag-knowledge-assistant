from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    DEBUG: bool

    HOST: str
    PORT: int
    MAX_FILE_SIZE: int
    CHUNK_SIZE: int
    CHUNK_OVERLAP: int
    EMBEDDING_MODEL: str
    EMBEDDING_DIMENSION: int
    QDRANT_URL: str
    QDRANT_API_KEY: str
    QDRANT_COLLECTION: str

    model_config = SettingsConfigDict(
    env_file=".env",
    env_file_encoding="utf-8",
    case_sensitive=True,
)

settings = Settings()