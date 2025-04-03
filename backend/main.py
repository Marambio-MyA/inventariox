from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routes.api_router import router as api_router
from routes.views_router import router as views_router
from starlette.middleware.sessions import SessionMiddleware  # ✅ CORRECTO

app = FastAPI()

# Clave secreta para las sesiones (debe ser segura y única)
app.add_middleware(SessionMiddleware, secret_key="TU_CLAVE_SECRETA")

# Incluir enrutadores
app.include_router(api_router, prefix="/api")  # Todas las rutas de la API estarán en /api
app.include_router(views_router)  # Las vistas no tienen prefijo

# Archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configuración de Jinja2
templates = Jinja2Templates(directory="templates")
