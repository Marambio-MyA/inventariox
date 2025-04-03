from fastapi import APIRouter
from .api import product_routes, user_routes, auth_routes

router = APIRouter()

# Registrar rutas de la API
router.include_router(product_routes.router, prefix="/productos", tags=["Productos"])
router.include_router(user_routes.router, prefix="/usuarios", tags=["Usuarios"])
router.include_router(auth_routes.router, prefix="/auth", tags=["Autenticación"])
