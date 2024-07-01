from django.contrib import admin
from django.urls import include, re_path
from . import views

urlpatterns = [
    re_path('home/', views.lista_productos),
    re_path('agregar/', views.agregar_producto),
    re_path('eliminar/', views.eliminar_producto),
]