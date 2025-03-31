import requests
import json

BASE_URL = "http://localhost:8000"

def test_crear_producto():
    """Prueba la creación de un producto"""
    producto = {
        "nombre": "Laptop HP",
        "descripcion": "Laptop HP 15 pulgadas",
        "cantidad_disponible": 10,
        "precio_unitario": 599.99,
        "categoria": "Electrónica"
    }
    
    response = requests.post(f"{BASE_URL}/productos/", json=producto)
    print("\nCrear Producto:")
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")
    return response.json()["id"] if response.status_code == 200 else None

def test_obtener_productos():
    """Prueba obtener todos los productos"""
    response = requests.get(f"{BASE_URL}/productos/")
    print("\nObtener Productos:")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

def test_obtener_producto(producto_id):
    """Prueba obtener un producto específico"""
    response = requests.get(f"{BASE_URL}/productos/{producto_id}")
    print("\nObtener Producto Específico:")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

def test_actualizar_producto(producto_id):
    """Prueba actualizar un producto"""
    producto_actualizado = {
        "precio_unitario": 649.99,
        "cantidad_disponible": 15
    }
    
    response = requests.put(f"{BASE_URL}/productos/{producto_id}", json=producto_actualizado)
    print("\nActualizar Producto:")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

def test_actualizar_stock(producto_id):
    """Prueba actualizar el stock de un producto"""
    response = requests.post(f"{BASE_URL}/productos/{producto_id}/stock?cantidad=-2")
    print("\nActualizar Stock:")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

def test_eliminar_producto(producto_id):
    """Prueba eliminar un producto"""
    response = requests.delete(f"{BASE_URL}/productos/{producto_id}")
    print("\nEliminar Producto:")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

def ejecutar_pruebas():
    """Ejecuta todas las pruebas en secuencia"""
    print("Iniciando pruebas de la API...")
    
    # Crear producto y obtener su ID
    producto_id = test_crear_producto()
    if not producto_id:
        print("Error: No se pudo crear el producto. Deteniendo pruebas.")
        return
    
    # Ejecutar resto de pruebas
    test_obtener_productos()
    test_obtener_producto(producto_id)
    test_actualizar_producto(producto_id)
    test_actualizar_stock(producto_id)
    test_eliminar_producto(producto_id)
    
    print("\nPruebas completadas.")

if __name__ == "__main__":
    ejecutar_pruebas() 