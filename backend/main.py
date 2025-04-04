from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routes.api_router import router as api_router
from routes.views_router import router as views_router
from starlette.middleware.sessions import SessionMiddleware
import config

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=config.SECRET_KEY_MIDDLEWARE)

# Incluir enrutadores
app.include_router(api_router, prefix="/api")
app.include_router(views_router)

# Archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configuración de Jinja2
templates = Jinja2Templates(directory="templates")
