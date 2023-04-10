
from functools import lru_cache
import uvicorn
import os

from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.openapi.utils import get_openapi

from local_server.config import Settings
 # load in settings right away before other modules to prevent circular dependency
settings = Settings()

from . import create_app
from local_server.routers import echo, solana
from local_server.dependencies import connect_solana

app = create_app()



solana_client = connect_solana()

PORT = settings.PORT

origins = [
    f"http://localhost:{PORT}",
    "https://chat.openai.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    print("printing the port - " + str(PORT))
    return {"Hello": "World"}

@app.route("/.well-known/ai-plugin.json")
async def get_manifest(request):
    file_path = "./local_server/ai-plugin.json"
    return FileResponse(file_path, media_type="text/json")


@app.route("/.well-known/logo.png")
async def get_logo(request):
    file_path = ".well-known/solana-sol-logo.png"

    return FileResponse(file_path, media_type="image/png")


@app.route("/.well-known/openapi.yaml")
async def get_openapi_endpoint(request):
    file_path = "./local_server/openapi.yaml"
    return FileResponse(file_path, media_type="text/json")


@lru_cache()
def get_settings():
    return Settings()


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Custom title",
        version="2.5.0",
        description="This is a very custom OpenAPI schema",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

def start():
    uvicorn.run(
        "local_server.main:app", 
        # host="localhost", 
        port=PORT, 
        reload=True,
        server_header=False
    )