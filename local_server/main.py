
from functools import lru_cache
import uvicorn
import os
import yaml

from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.openapi.utils import get_openapi
from fastapi import FastAPI

from local_server.config import settings

# from . import create_app
from local_server.dependencies import solana_client


from local_server.routers import echo, solana

app = FastAPI()
app.include_router(echo.router)
app.include_router(solana.router)





PORT = settings.PORT
print("PORT: " + str(PORT))

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
    file_path = "./.well-known/ai-plugin.json"
    print('well known ai-plugin')
    return FileResponse(file_path, media_type="text/json")


@app.route("/.well-known/logo.png")
async def get_logo(request):
    file_path = "./.well-known/solana-sol-logo.png"

    return FileResponse(file_path, media_type="image/png")


@app.route("/.well-known/openapi.yaml")
async def get_openapi_endpoint(request):
    file_path = "./.well-known/openapi.yaml"
    return FileResponse(file_path, media_type="text/json")


favicon_path = '/saluting-face_1fae1.ico'

@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)


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

with open(".well-known/openapi.yaml", 'w') as openapi_yaml: 
    openapi_yaml.write(yaml.dump(app.openapi()))

def start():
    uvicorn.run(
        "local_server.main:app", 
        # host="localhost", 
        port=PORT, 
        reload=True,
        server_header=False
    )