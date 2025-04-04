import os
from dotenv import load_dotenv

load_dotenv()

# Configuración de la base de datos PostgreSQL
DB_USER = os.getenv('POSTGRES_USER')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB_SERVER = os.getenv('POSTGRES_SERVER')
DB_NAME = os.getenv('POSTGRES_DB')

# Configuración de seguridad
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

# Configuración de Middleware
SECRET_KEY_MIDDLEWARE = os.getenv("SECRET_KEY_MIDDLEWARE")

# Configuración de la API
API_BACKEND = os.getenv("API_BACKEND")