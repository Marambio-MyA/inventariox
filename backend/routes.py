from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from pydantic import BaseModel
from database.database import get_db, engine
from services.producto_service import ProductoService
from models.product_model import Base

# Crear las tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema de Inventario")

class ProductoBase(BaseModel):
    nombre: str
    descripcion: str
    cantidad_disponible: int
    precio_unitario: float
    categoria: str

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    cantidad_disponible: Optional[int] = None
    precio_unitario: Optional[float] = None
    categoria: Optional[str] = None

class Producto(ProductoBase):
    id: int
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    class Config:
        from_attributes = True

@app.get("/productos/", response_model=List[Producto])
def listar_productos(
    skip: int = 0,
    limit: int = 100,
    categoria: Optional[str] = None,
    db: Session = Depends(get_db)
):
    return ProductoService.get_productos(db, skip, limit, categoria)

@app.post("/productos/", response_model=Producto)
def crear_producto(producto: ProductoCreate, db: Session = Depends(get_db)):
    return ProductoService.crear_producto(db, producto.model_dump())

@app.get("/productos/{producto_id}", response_model=Producto)
def obtener_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = ProductoService.get_producto(db, producto_id)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@app.put("/productos/{producto_id}", response_model=Producto)
def actualizar_producto(
    producto_id: int,
    producto: ProductoUpdate,
    db: Session = Depends(get_db)
):
    db_producto = ProductoService.actualizar_producto(db, producto_id, producto.model_dump(exclude_unset=True))
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto

@app.delete("/productos/{producto_id}")
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    if not ProductoService.eliminar_producto(db, producto_id):
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"message": "Producto eliminado exitosamente"}

@app.post("/productos/{producto_id}/stock")
def actualizar_stock(
    producto_id: int,
    cantidad: int,
    db: Session = Depends(get_db)
):
    producto = ProductoService.actualizar_stock(db, producto_id, cantidad)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto
