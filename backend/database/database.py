from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import config

Base = declarative_base()

def crear_base_datos():
    """Crea la base de datos si no existe usando SQLAlchemy"""
    engine = create_engine(f"postgresql://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_SERVER}/postgres", isolation_level="AUTOCOMMIT")
    
    with engine.connect() as conn:
        # Verificar si la base de datos existe
        result = conn.execute(text(f"SELECT 1 FROM pg_database WHERE datname = '{config.DB_NAME}'"))
        existe = result.scalar()

        if not existe:
            # Crear la base de datos
            conn.execute(text(f'CREATE DATABASE {config.DB_NAME}'))
            print(f"Base de datos '{config.DB_NAME}' creada exitosamente")
        else:
            print(f"La base de datos '{config.DB_NAME}' ya existe")

def crear_tablas():
    """Crea las tablas si no existen"""
    engine = create_engine(f"postgresql://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_SERVER}/{config.DB_NAME}")
    
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas/verificadas exitosamente")

# Crear la base de datos si no existe
crear_base_datos()

# URL de la base de datos
DATABASE_URL = f"postgresql://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_SERVER}/{config.DB_NAME}"

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
