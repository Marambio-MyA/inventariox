from sqlalchemy.orm import Session
from models.product_model import Producto
from typing import List, Optional
            
class ProductoService:
    @staticmethod
    def get_productos(db: Session, skip: int = 0, limit: int = 100, categoria: Optional[str] = None) -> List[Producto]:
        query = db.query(Producto)
        if categoria:
            query = query.filter(Producto.categoria == categoria)
        return query.offset(skip).limit(limit).all()

    @staticmethod
    def get_producto(db: Session, producto_id: int) -> Optional[Producto]:
        return db.query(Producto).filter(Producto.id == producto_id).first()

    @staticmethod
    def crear_producto(db: Session, producto_data: dict) -> Producto:
        db_producto = Producto(**producto_data)
        db.add(db_producto)
        db.commit()
        db.refresh(db_producto)
        return db_producto

    @staticmethod
    def actualizar_producto(db: Session, producto_id: int, producto_data: dict) -> Optional[Producto]:
        db_producto = db.query(Producto).filter(Producto.id == producto_id).first()
        if db_producto:
            for key, value in producto_data.items():
                setattr(db_producto, key, value)
            db.commit()
            db.refresh(db_producto)
        return db_producto

    @staticmethod
    def eliminar_producto(db: Session, producto_id: int) -> bool:
        db_producto = db.query(Producto).filter(Producto.id == producto_id).first()
        if db_producto:
            db.delete(db_producto)
            db.commit()
            return True
        return False

    @staticmethod
    def actualizar_stock(db: Session, producto_id: int, cantidad: int) -> Optional[Producto]:
        db_producto = db.query(Producto).filter(Producto.id == producto_id).first()
        if db_producto:
            nueva_cantidad = db_producto.cantidad_disponible + cantidad
            if nueva_cantidad >= 0:
                db_producto.cantidad_disponible = nueva_cantidad
                db.commit()
                db.refresh(db_producto)
        return db_producto 