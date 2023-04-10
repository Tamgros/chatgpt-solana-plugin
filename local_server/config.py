from pydantic import BaseSettings
from dotenv import load_dotenv
# from pathlib import Path
import os

# load_dotenv(dotenv_path=Path("~/local-server/.env"))
load_dotenv()

class BaseConfig(BaseSettings):
    DEFAULT_VAR="some default string value"  # default value if env variable does not exist
    API_KEY: str=''
    APP_MAX: int=100 # default value if env variable does not exist
    PORT: int=os.getenv("PORT")
    SOLANA_RPC: str="https://api.devnet.solana.com"

    # class Config:
    #     env_file = '~/.env'
    #     env_file_encoding = 'utf-8'
    #     case_sensitive = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    SOLANA_RPC ="https://api.devnet.solana.com"


class ProductionConfig(BaseConfig):
    """Production configuration."""
    DEBUG = False
    SOLANA_RPC = "https://api.mainnet-beta.solana.com"


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SOLANA_RPC = "https://api.testnet.solana.com"


dev_env = os.getenv("DEV_ENV")


if dev_env == 'development':
    Settings = DevelopmentConfig
elif dev_env == 'production':
    Settings = ProductionConfig
elif dev_env == 'testing':
    Settings = TestingConfig
else:
    raise ValueError(f"Invalid DEV_ENV value: {dev_env}")


settings = Settings()