import csv
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import BaseRenderer
from datetime import datetime  
from rest_framework.authtoken.models import Token
from .models import Pais, Autor, Editorial, Idioma, Libro, Genero, Region, Ciudad, Comuna, Bodega, Usuario, Movimiento
from .serializers import PaisSerializer, AutorSerializer, EditorialSerializer, IdiomaSerializer, LibroSerializer, GeneroSerializer, RegionSerializer, CiudadSerializer, ComunaSerializer, BodegaSerializer, UsuarioSerializer, MovimientoSerializer 
from django.shortcuts import get_object_or_404, redirect


# Create your views here.

@api_view(['POST'])
def agregar_producto(request):
    serializer = LibroSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
        return Response({'mensaje': 'Libro agregado exitosamente'}, status=201)
    else:
        return Response({'errores': serializer.errors}, status=400)

@api_view(['GET'])
def lista_productos(request):
    libros = Libro.objects.all().order_by('id_libro')
    serializer = LibroSerializer(libros, many=True)
    return Response(serializer.data, status=200)

@api_view(['POST'])
def registrar_entrada(request):
    data = request.data.copy()
    data['tipo_movimiento'] = 'entrada'
    serializer = MovimientoSerializer(data=data)
    if serializer.is_valid():
        serializer.save(tipo_movimiento='entrada')
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def registrar_salida(request):
    data = request.data.copy()
    data['tipo_movimiento'] = 'salida'
    serializer = MovimientoSerializer(data=data)
    if serializer.is_valid():
        serializer.save(tipo_movimiento='salida')
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def registrar_traslado(request):
    serializer = MovimientoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(tipo_movimiento='traslado')
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def generar_informe(request):
    informe = Movimiento.objects.all().order_by('id_movimiento')
    serializer = MovimientoSerializer(informe, many=True)
    return Response(serializer.data, status=200)
    
