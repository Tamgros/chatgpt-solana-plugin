from pydantic import BaseSettings
from dotenv import load_dotenv
# from pathlib import Path
import os
import json

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


ai_plugin_content = {
    "schema_version": "v1",
    "name_for_model": "Solana_Transcaction",
    "name_for_human": "Solana_Plugin",
    "description_for_model": "Plugin querying from and sending transactions to the Solana blockchain. Use it when a user wants to create or send Tokens",
    "description_for_human": "Search through your documents.",
    "auth": {
        "type": "none"
      },
      "api": {
        "type": "openapi",
        "url": f"http://localhost:{settings.PORT}/.well-known/openapi.yaml",
        "is_user_authenticated": "false"
      },
      "logo_url": f"http://localhost:{settings.PORT}/.well-known/logo.png",
      "contact_email": "sorg.matthew@gmail.com", 
      "legal_info_url": "sorg.matthew@gamil.com"
}

ai_plugin_json = json.dumps(ai_plugin_content)

with open('./.well-known/ai-plugin.json', "w+") as plugin_file:  

    json.dump(ai_plugin_content, plugin_file, indent=4)
