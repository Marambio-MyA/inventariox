from fastapi import APIRouter
from routes.views import login_view, home_view, productos, entradas_salidas

router = APIRouter()

#Vistas del usuario
router.include_router(home_view.router, prefix="", tags=["Home"])
router.include_router(login_view.router, prefix="", tags=["Login"])
router.include_router(productos.router, prefix="", tags=["Login"])
router.include_router(entradas_salidas.router, prefix="", tags=["Login"])

