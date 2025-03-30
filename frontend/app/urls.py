from django.urls import path
from .views import *

urlpatterns = [
    path("login/", login_view, name="login"),  # Login
    path('home/', home, name='home'),
    path('actualizar/', actualizar_producto, name='actualizar'),
    path('entradas_salidas/', entradas_salidas, name='entradas_salidas'),
]
