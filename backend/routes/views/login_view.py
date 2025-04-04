from fastapi import APIRouter, Request, Depends, Form, HTTPException
from fastapi.templating import Jinja2Templates
from schemas.views.login_schema import Login
from sqlalchemy.orm import Session
from database.database import get_db
from models.user_model import Usuario
from fastapi.responses import RedirectResponse
from .utils import from_api

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/login")
def dashboard(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# Autenticación de usuario
@router.post("/login", name="login_action")
async def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
):
    # Definimos la ruta del endpoint de autenticación
    ruta = "/api/auth/token"  # El endpoint de autenticación
    data = {"username": username, "password": password}
    
    try:
        # Realizamos la solicitud a la API para obtener el token
        response = await from_api(ruta, metodo="POST", data=data)
        
        # Si la solicitud es exitosa, obtenemos el token
        access_token = response.get("access_token")
        
        if access_token:
            # Guardamos el token en la sesión
            request.session["access_token"] = access_token
            return RedirectResponse(url="/", status_code=303)
        else:
            return templates.TemplateResponse("login.html", {
                "request": request,
                "error": "Usuario o contraseña incorrectos"
            })
    
    except HTTPException as e:
        return templates.TemplateResponse("login.html", {
            "request": request,
            "error": f"Error en la autenticación: {e.detail}"
        })