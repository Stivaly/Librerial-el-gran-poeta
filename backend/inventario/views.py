from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import Pais, Autor, Editorial, Idioma, Libro, Genero, Region, Ciudad, Comuna, Bodega, Usuario, Movimiento
from .serializers import PaisSerializer, AutorSerializer, EditorialSerializer, IdiomaSerializer, LibroSerializer, GeneroSerializer, RegionSerializer, CiudadSerializer, ComunaSerializer, BodegaSerializer, UsuarioSerializer, MovimientoSerializer 
from django.shortcuts import get_object_or_404, redirect

# Create your views here.

@api_view(['POST'])
def agregar_producto(request):
    libro = LibroSerializer(data=request.data.get('libro'))
    bodega = BodegaSerializer(data=request.data.get('bodega'))
    if libro.is_valid() and bodega.is_valid():
         return Response({'mensaje': 'Producto agregado exitosamente'}, status=201)
    else:
        return Response({'errores': libro.errors + bodega.errors}, status=400)
    
@api_view(['DELETE'])
def eliminar_producto(request, id):
    libro = get_object_or_404(LibroSerializer, id=id)
    libro.delete()
    return Response({'mensaje': 'Producto eliminado exitosamente'}, status=200)

@api_view(['GET'])
def lista_productos(request):
    libros = Libro.objects.all()
    serializer = LibroSerializer(libros, many=True)
    return Response(serializer.data, status=200)


    
    