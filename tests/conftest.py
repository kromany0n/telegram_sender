from pydantic import BaseSettings
import pytest

class Config(BaseSettings):
    bot_token: str
    chat_id: int

    class Config: # pyright: ignore
        env_file = '.env'

@pytest.fixture(scope='session')
def config():
    return Config() # pyright: ignore
