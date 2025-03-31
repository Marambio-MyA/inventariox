import os
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# Obtener variables de entorno
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "inventariox")

# URL de conexión para crear la base de datos
DB_URL_CREATE = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/postgres"

def crear_base_datos():
    """Crea la base de datos si no existe"""
    # Crear conexión a postgres (base de datos por defecto)
    engine = create_engine(DB_URL_CREATE)
    
    # Verificar si la base de datos existe
    with engine.connect() as conn:
        result = conn.execute(text(f"SELECT 1 FROM pg_database WHERE datname = '{DB_NAME}'"))
        if not result.scalar():
            # Cerrar todas las conexiones antes de crear la base de datos
            conn.close()
            
            # Crear la base de datos
            with engine.connect() as conn:
                conn.execute(text("COMMIT"))  # Cerrar cualquier transacción pendiente
                conn.execute(text(f'CREATE DATABASE {DB_NAME}'))
                conn.close()

# Crear la base de datos si no existe
crear_base_datos()

# URL de conexión para la aplicación
SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Crear el motor de SQLAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Crear la clase SessionLocal
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear la clase Base
Base = declarative_base()

# Función para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def crear_tablas():
    """Crea las tablas si no existen"""
    # Crear engine con la base de datos específica
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    
    # Crear todas las tablas
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas/verificadas exitosamente")

# Crear las tablas al iniciar
crear_tablas()
