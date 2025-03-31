from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

# Definir Base antes de usarlo
Base = declarative_base()

# Obtener credenciales sin el nombre de la base de datos
DB_USER = os.getenv('POSTGRES_USER')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB_SERVER = os.getenv('POSTGRES_SERVER')
DB_NAME = os.getenv('POSTGRES_DB')

def crear_base_datos():
    """Crea la base de datos si no existe usando SQLAlchemy"""
    # Crear engine con autocommit=True para evitar el error de transacción activa
    engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/postgres", isolation_level="AUTOCOMMIT")
    
    with engine.connect() as conn:
        # Verificar si la base de datos existe
        result = conn.execute(text(f"SELECT 1 FROM pg_database WHERE datname = '{DB_NAME}'"))
        existe = result.scalar()

        if not existe:
            # Crear la base de datos
            conn.execute(text(f'CREATE DATABASE {DB_NAME}'))
            print(f"Base de datos '{DB_NAME}' creada exitosamente")
        else:
            print(f"La base de datos '{DB_NAME}' ya existe")

def crear_tablas():
    """Crea las tablas si no existen"""
    # Crear engine con la base de datos específica
    engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}")
    
    # Crear todas las tablas
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas/verificadas exitosamente")

# Crear la base de datos si no existe
crear_base_datos()

# URL de la base de datos
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}"

# Crear engine y sesión
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Crear las tablas al iniciar
crear_tablas()
