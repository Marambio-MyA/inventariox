from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class UsuarioCreate(BaseModel):
    nombre: str
    nombre_usuario: str
    email: EmailStr
    contraseña: str

class Usuario(UsuarioCreate):
    id: int

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    nombre_usuario: Optional[str] = None
