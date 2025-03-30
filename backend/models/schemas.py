from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class ProductoBase(BaseModel):
    nombre: str
    descripcion: str
    cantidad_disponible: int = Field(ge=0)
    precio_unitario: float = Field(ge=0)
    categoria: str

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    cantidad_disponible: Optional[int] = Field(None, ge=0)
    precio_unitario: Optional[float] = Field(None, ge=0)
    categoria: Optional[str] = None

class Producto(ProductoBase):
    id: int

    class Config:
        from_attributes = True

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
