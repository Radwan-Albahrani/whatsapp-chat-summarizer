from pydantic import SecretStr, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class GeminiApi(BaseSettings):
    key: SecretStr
    prompt: str = """
    You will be given a list of messages. Read them, Extract the main points, and give a brief summary of the messages.

    The summary should highlight the main points of the messages, while mentioning the sender of the messages.

    Messages:

    {messages}
"""

    @model_validator(mode="before")
    def validate_model(cls, v):
        return {
            "key": v["key"],
        }

    class Config(SettingsConfigDict):
        env_prefix = "GEMINI_API_"
        env_file = ".env"
        extra = "ignore"
