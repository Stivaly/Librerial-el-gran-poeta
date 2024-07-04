from django.urls import re_path
from . import views

urlpatterns = [
    re_path('home/', views.lista_productos),
    re_path('agregar/', views.agregar_producto),
    re_path('movimiento/entrada/', views.registrar_entrada),
    re_path('movimiento/salida/', views.registrar_salida),
    re_path('movimiento/traslado/', views.registrar_traslado),
]

