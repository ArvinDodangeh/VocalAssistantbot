import os
from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    openai_key: str = Field(..., validation_alias='OpenAi_Key')
    telegram_token: str = Field(..., alias='Telegram_API')

    class Config:
        env_file = os.path.join(os.path.dirname(__file__), '../.env')


setting = Settings()
