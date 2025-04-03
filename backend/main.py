from fastapi import FastAPI
from routes.user_routes import router as user_router
from routes.product_routes import router as product_router
from routes.auth_routes import router as auth_router
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")
app = FastAPI()


# Incluir enrutadores
app.include_router(user_router, prefix="/users", tags=["Usuarios"])
app.include_router(product_router, prefix="/productos", tags=["Productos"])
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
