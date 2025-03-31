import requests
import json

BASE_URL = "http://localhost:8000"

def test_crear_usuario():
    """Prueba la creación de un usuario"""
    usuario = {
        "nombre": "Admin",
        "nombre_usuario": "admin",
        "email": "admin@example.com",
        "contraseña": "admin123"
    }
    
    response = requests.post(f"{BASE_URL}/usuarios/", json=usuario)
    print("\nCrear Usuario:")
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")
    return response.status_code == 200

def test_login():
    """Prueba el login y obtiene el token"""
    data = {
        "username": "admin",
        "password": "admin123"
    }
    
    response = requests.post(f"{BASE_URL}/token", data=data)
    print("\nLogin:")
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")
    
    if response.status_code == 200:
        return response.json()["access_token"]
    return None

def test_crear_producto(token):
    """Prueba la creación de un producto"""
    producto = {
        "nombre": "Laptop HP",
        "descripcion": "Laptop HP 15 pulgadas",
        "cantidad_disponible": 10,
        "precio_unitario": 599.99,
        "categoria": "Electrónica"
    }
    
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{BASE_URL}/productos/", json=producto, headers=headers)
    print("\nCrear Producto:")
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")
    return response.json()["id"] if response.status_code == 200 else None

def test_obtener_productos(token):
    """Prueba obtener todos los productos"""
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/productos/", headers=headers)
    print("\nObtener Productos:")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

def test_obtener_producto(producto_id, token):
    """Prueba obtener un producto específico"""
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/productos/{producto_id}", headers=headers)
    print("\nObtener Producto Específico:")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

def test_actualizar_producto(producto_id, token):
    """Prueba actualizar un producto"""
    producto_actualizado = {
        "precio_unitario": 649.99,
        "cantidad_disponible": 15
    }
    
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.put(f"{BASE_URL}/productos/{producto_id}", json=producto_actualizado, headers=headers)
    print("\nActualizar Producto:")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

def test_actualizar_stock(producto_id, token):
    """Prueba actualizar el stock de un producto"""
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{BASE_URL}/productos/{producto_id}/stock?cantidad=-2", headers=headers)
    print("\nActualizar Stock:")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

def test_eliminar_producto(producto_id, token):
    """Prueba eliminar un producto"""
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.delete(f"{BASE_URL}/productos/{producto_id}", headers=headers)
    print("\nEliminar Producto:")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

def ejecutar_pruebas():
    """Ejecuta todas las pruebas en secuencia"""
    print("Iniciando pruebas de la API...")
    
    # Crear usuario y obtener token
    if not test_crear_usuario():
        print("Error: No se pudo crear el usuario. Deteniendo pruebas.")
        return
    
    token = test_login()
    if not token:
        print("Error: No se pudo obtener el token. Deteniendo pruebas.")
        return
    
    # Crear producto y obtener su ID
    producto_id = test_crear_producto(token)
    if not producto_id:
        print("Error: No se pudo crear el producto. Deteniendo pruebas.")
        return
    
    # Ejecutar resto de pruebas
    test_obtener_productos(token)
    test_obtener_producto(producto_id, token)
    test_actualizar_producto(producto_id, token)
    test_actualizar_stock(producto_id, token)
    test_eliminar_producto(producto_id, token)
    
    print("\nPruebas completadas.")

if __name__ == "__main__":
    ejecutar_pruebas() 