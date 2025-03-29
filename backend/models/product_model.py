from sqlalchemy import Column, Integer, String, Float, DateTime, CheckConstraint
from sqlalchemy.sql import func
from database.database import Base

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String, nullable=False)
    cantidad_disponible = Column(Integer, nullable=False)
    precio_unitario = Column(Float, nullable=False)
    categoria = Column(String, nullable=False)

    __table_args__ = (
        CheckConstraint('cantidad_disponible >= 0', name='check_cantidad_positiva'),
        CheckConstraint('precio_unitario >= 0', name='check_precio_positivo'),
    ) 
