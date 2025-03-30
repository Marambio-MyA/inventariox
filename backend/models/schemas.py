from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

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
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True  # Nuevo nombre para orm_mode en Pydantic v2
