# Configuración de la API
API_BASE_URL = "http://localhost:8001"  # URL del backend FastAPI

# Configuración de autenticación
AUTH_ENDPOINTS = {
    "login": f"{API_BASE_URL}/token",
    "register": f"{API_BASE_URL}/usuarios/",
}

# Configuración de productos
PRODUCT_ENDPOINTS = {
    "list": f"{API_BASE_URL}/productos/",
    "detail": f"{API_BASE_URL}/productos/{{id}}/",
    "create": f"{API_BASE_URL}/productos/",
    "update": f"{API_BASE_URL}/productos/{{id}}",
    "delete": f"{API_BASE_URL}/productos/{{id}}",
    "update_stock": f"{API_BASE_URL}/productos/{{id}}/stock",
} 