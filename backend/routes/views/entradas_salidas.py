from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from .utils import get_current_user

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/movimientos")
def movimientos(request: Request):
    user = get_current_user(request)
    if not user:
        return RedirectResponse(url="/login", status_code=303)
    return templates.TemplateResponse("entradas_salidas.html", {"request": request, "user": user})
