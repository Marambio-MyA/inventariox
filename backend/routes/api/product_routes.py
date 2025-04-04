from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from typing import List, Optional
from database.database import get_db
from services.product_service import ProductoService
from schemas.api.producto_schemas import (
    ProductoCreate,
    ProductoUpdate,
    ProductoUpdateCantidad,
    Producto
)
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io


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

@router.get("/reporte/pdf")
def generar_reporte_pdf(db: Session = Depends(get_db)):
    productos = db.query(Producto).all()
    
    total_productos = len(productos)
    valor_total = sum(prod.precio * prod.cantidad for prod in productos)
    productos_agotados = [prod.nombre for prod in productos if prod.cantidad == 0]

    # Crear PDF en memoria
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    pdf.setTitle("Reporte de Inventario")

    pdf.drawString(100, 750, "Reporte de Inventario")
    pdf.drawString(100, 730, f"Total de productos: {total_productos}")
    pdf.drawString(100, 710, f"Valor total del inventario: ${valor_total:.2f}")
    
    pdf.drawString(100, 690, "Productos agotados:")
    y = 670
    for producto in productos_agotados:
        pdf.drawString(120, y, f"- {producto}")
        y -= 20
    
    pdf.save()
    buffer.seek(0)

    # Devolver el PDF como respuesta
    return Response(content=buffer.getvalue(), media_type="application/pdf", headers={
        "Content-Disposition": "attachment; filename=Reporte.pdf"
    })