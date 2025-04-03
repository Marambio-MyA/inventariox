from sqlalchemy.orm import Session
from models.user_model import Usuario
from passlib.context import CryptContext
from typing import Optional
from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import HTTPException, status
from dotenv import load_dotenv
import os

load_dotenv()

# Configuración de seguridad
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('HS256')
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv('ACCES_TOKEN_EXPIRE_MINUTES')

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService:
    @staticmethod
    def verificar_contraseña(contraseña_plana: str, contraseña_hash: str) -> bool:
        return pwd_context.verify(contraseña_plana, contraseña_hash)

    @staticmethod
    def obtener_hash_contraseña(contraseña: str) -> str:
        return pwd_context.hash(contraseña)

    @staticmethod
    def crear_usuario(db: Session, usuario_data: dict) -> Usuario:
        # Verificar si el usuario ya existe
        if db.query(Usuario).filter(Usuario.nombre_usuario == usuario_data["nombre_usuario"]).first():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El nombre de usuario ya está registrado"
            )
        if db.query(Usuario).filter(Usuario.email == usuario_data["email"]).first():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El email ya está registrado"
            )
        
        # Hashear la contraseña antes de guardar
        usuario_data["contraseña"] = AuthService.obtener_hash_contraseña(usuario_data["contraseña"])
        db_usuario = Usuario(**usuario_data)
        db.add(db_usuario)
        db.commit()
        db.refresh(db_usuario)
        return db_usuario

    @staticmethod
    def autenticar_usuario(db: Session, nombre_usuario: str, contraseña: str) -> Optional[Usuario]:
        usuario = db.query(Usuario).filter(Usuario.nombre_usuario == nombre_usuario).first()
        if not usuario:
            return None
        if not AuthService.verificar_contraseña(contraseña, usuario.contraseña):
            return None
        return usuario

    @staticmethod
    def crear_token_acceso(data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    @staticmethod
    def verificar_token(token: str) -> dict:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return payload
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="No se pudo validar la credencial",
                headers={"WWW-Authenticate": "Bearer"},
            ) 