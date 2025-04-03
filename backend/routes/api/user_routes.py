from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from database.database import get_db
from services.auth_service import AuthService
from schemas.api.user_schemas import (
    UsuarioCreate,
    Usuario
)

router = APIRouter()

@router.post("/usuarios/", response_model=Usuario)
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return AuthService.crear_usuario(db, usuario.model_dump())