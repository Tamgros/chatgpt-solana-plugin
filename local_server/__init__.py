import os

from .routers import echo, solana

# from src.chatgpt_plugin.app.solana.solana_client import connect_solana

from fastapi import FastAPI

def create_app():
    # app = Quart(__name__)
    app = FastAPI()



    # @app.before_request
    # def before_request():
    #     if 'solana_client' not in g:
    #         g.solana_client = connect_solana(app.config) 


    # cors(app, allow_origin=[f"http://localhost:{PORT}", "https://chat.openai.com"])

    # Set the configuration based on the environment variable 'FLASK_ENV'

    

    app.include_router(echo.router)
    app.include_router(solana.router)
    
    
    return app