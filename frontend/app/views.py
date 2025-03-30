from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def login_view(request):
    return render(request, "app/login.html")

# Vista para la página de inicio (Dashboard)
def home(request):
    return render(request, 'app/home.html')

# Vista para la actualización de producto
def actualizar_producto(request):
    return render(request, 'app/actualizar_producto.html')

# Vista para la gestión de entradas y salidas de inventario
def entradas_salidas(request):
    return render(request, 'app/entradas_salidas.html')