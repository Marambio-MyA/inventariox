from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from typing import List, Optional
from database.database import get_db
from services.product_service import ProductoService
from schemas.producto_schemas import (
    ProductoCreate,
    ProductoUpdate,
    ProductoUpdateCantidad,
    Producto
)

router = APIRouter()

# Configuración de OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

# Rutas de productos (protegidas)
@router.get("/", response_model=List[Producto])
def listar_productos(
    skip: int = 0,
    limit: int = 100,
    categoria: Optional[str] = None,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    return ProductoService.get_productos(db, skip, limit, categoria)

@router.post("/", response_model=Producto)
def crear_producto(
    producto: ProductoCreate,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    return ProductoService.crear_producto(db, producto.model_dump())

@router.get("/{producto_id}", response_model=Producto)
def obtener_producto(
    producto_id: int,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    producto = ProductoService.get_producto(db, producto_id)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.put("/{producto_id}", response_model=Producto)
def actualizar_producto(
    producto_id: int,
    producto: ProductoUpdate,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    db_producto = ProductoService.actualizar_producto(db, producto_id, producto.model_dump(exclude_unset=True))
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto

@router.delete("/{producto_id}")
def eliminar_producto(
    producto_id: int,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    if not ProductoService.eliminar_producto(db, producto_id):
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"message": "Producto eliminado exitosamente"}

@router.patch("/{producto_id}")
def actualizar_stock(
    producto_id: int,
    producto: ProductoUpdateCantidad,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    producto = ProductoService.actualizar_stock(db, producto_id, producto.cantidad_disponible)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

