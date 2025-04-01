from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import requests
from django.conf import settings
from dotenv import load_dotenv
from django.contrib.auth import login as django_login
from django.contrib.auth.models import AnonymousUser



load_dotenv()

# Vista para el login (si es necesario)
def login_view(request):
    if request.method == "POST":
        data = {"username": request.POST["username"], "password": request.POST["password"]}

        try:
            response = requests.post(f"{settings.FASTAPI_URL}/token", data=data)
            if response.status_code == 200:
                access_token = response.json().get("access_token")
                request.session['access_token'] = access_token

                user_response = requests.get(
                    f"{settings.FASTAPI_URL}/users/me", 
                    headers={"Authorization": f"Bearer {access_token}"}
                )
                if user_response.status_code == 200:
                    django_login(request, AnonymousUser())
                    messages.success(request, "Inicio de sesión exitoso.")
                    return redirect('/app/home/')
                else:
                    messages.error(request, "Error al obtener los datos del usuario.")
            else:
                messages.error(request, "Usuario o contraseña incorrectos.")
        except requests.exceptions.RequestException:
            messages.error(request, "Error al conectar con la API.")

    return render(request, "app/login.html")

# Vista para el Dashboard/Home
login_required
def home(request):
    return render(request, "app/home.html")

# Vista para listar productos
#@login_required
def listar_productos(request):
    # Aquí puedes obtener los productos desde la base de datos y pasarlos al template
    productos = []  # Simulación de productos, reemplazar con consulta real
    return render(request, "app/productos/listar.html", {'productos': productos})

# Vista para crear producto
#@login_required
def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio_unitario = request.POST.get('precio')
        categoria = request.POST.get('categoria')
        cantidad_disponible = request.POST.get('stock')

        # Crear los datos del producto para la API
        producto_data = {
            'nombre': nombre,
            'descripcion': "",  # Puedes agregar una descripción si lo deseas
            'cantidad_disponible': int(cantidad_disponible),
            'precio_unitario': float(precio_unitario),
            'categoria': categoria
        }

        # Enviar la solicitud POST a la API de FastAPI
        response = requests.post('http://localhost:8000/productos/', json=producto_data)

        if response.status_code == 201:
            messages.success(request, 'Producto creado exitosamente.')
            return redirect('listar_productos')  # Redirige a la lista de productos
        else:
            messages.error(request, 'Error al crear el producto.')

    return render(request, "app/productos/crear.html")

# Vista para actualizar producto
#@login_required
def actualizar_producto(request, id):
    return render(request, "app/productos/actualizar.html", {'id': id})

# Vista para gestionar entradas y salidas
#@login_required
def entradas_salidas(request):
    return render(request, "app/inventario/entradas_salidas.html")
