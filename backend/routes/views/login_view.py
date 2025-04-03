from fastapi import APIRouter, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordBearer
from schemas.views.login_schema import Login
from sqlalchemy.orm import Session
from database.database import get_db
from models.user_model import Usuario
from fastapi.responses import RedirectResponse

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/login")
def dashboard(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# Autenticación de usuario
@router.post("/login", name="login_action")
async def login(
    request: Request,
    username: str = Form(...),  # ⬅️ Recibir username desde el formulario
    password: str = Form(...), 
    db: Session = Depends(get_db)
    
    ):
    user = db.query(Usuario).filter(Usuario.nombre_usuario == username, Usuario.contraseña == password).first()
    if user:
        request.session["user"] = {"username": user.username}
        return RedirectResponse(url="/dashboard", status_code=303)
    return templates.TemplateResponse("home.html", {"request": request, "error": "Usuario o contraseña incorrectos"})