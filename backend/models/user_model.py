from sqlalchemy import Column, Integer, String, DateTime
from database.database import Base,engine

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    nombre_usuario = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    contraseña = Column(String, nullable=False)
    
Usuario.metadata.create_all(bind=engine)