from django.urls import path
from .views import login_view, home, listar_productos, crear_producto, actualizar_producto, entradas_salidas

urlpatterns = [
    path("login/", login_view, name="login"),
    path("home/", home, name="home"),
    
    # Rutas para los productos
    path("productos/", listar_productos, name="listar_productos"),
    path("productos/crear/", crear_producto, name="crear_producto"),
    path("productos/actualizar/<int:id>/", actualizar_producto, name="actualizar_producto"),
    path("productos/detalle/<int:id>/", listar_productos, name="detalle_producto"),

    # Rutas para la gestión de inventario
    path("entradas-salidas/", entradas_salidas, name="entradas_salidas"),
]
