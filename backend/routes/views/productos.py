from fastapi import APIRouter, Request, Query
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from .utils import get_current_user, from_api

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/productos")
async def productos(
    request: Request,
    search: str = Query(None),
    categoria: str = Query(None),
    stock: str = Query(None)  # 'disponible' o 'agotado'
):
    user = get_current_user(request)
    
    if not user:
        return RedirectResponse(url="/login", status_code=303)

    headers = {"Authorization": f"Bearer {user['access_token']}"}

    # Armamos la URL con los filtros
    ruta = "/productos?"
    if categoria:
        ruta += f"categoria={categoria}&"
    
    productos = await from_api(ruta, headers=headers)

    # Aplicamos filtros manuales si es necesario
    if search:
        productos = [p for p in productos if search.lower() in p["nombre"].lower()]
    
    if stock:
        if stock == "disponible":
            productos = [p for p in productos if p["cantidad_disponible"] > 0]
        elif stock == "agotado":
            productos = [p for p in productos if p["cantidad_disponible"] == 0]

    # Obtener todas las categorías distintas
    categorias = list(set(p["categoria"] for p in productos))

    return templates.TemplateResponse("productos.html", {
        "request": request,
        "user": user,
        "productos": productos,
        "categorias": categorias,
        "search": search or "",
        "selected_categoria": categoria or "",
        "selected_stock": stock or ""
    })
