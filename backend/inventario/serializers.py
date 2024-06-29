from rest_framework import serializers
from django.contrib.auth.models import models
from .models import Pais, Autor, Editorial, Idioma, Libro, Genero, Region, Ciudad, Comuna, Bodega, Usuario, Movimiento

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = '__all__'
        
class AutorSerializer(serializers.ModelSerializer):
    pais = PaisSerializer()
    
    class Meta:
        model = Autor
        fields = '__all__'
        
class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = '__all__'
        
class IdiomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idioma
        fields = '__all__'
        
        
class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'
        
class LibroSerializer(serializers.ModelSerializer):
    editorial = EditorialSerializer()
    autor = AutorSerializer()
    idioma = IdiomaSerializer()
    genero = GeneroSerializer()
    
    class Meta:
        model = Libro
        fields = '__all__'
        
class RegionSerializer(serializers.ModelSerializer):
    pais = PaisSerializer()
    
    class Meta:
        model = Region
        fields = '__all__'
        
class CiudadSerializer(serializers.ModelSerializer):
    region = RegionSerializer()
    
    class Meta:
        model = Ciudad
        fields = '__all__'
        
class ComunaSerializer(serializers.ModelSerializer):
    region = RegionSerializer()
    ciudad = CiudadSerializer()
    
    class Meta:
        model = Comuna
        fields = '__all__'

class BodegaSerializer(serializers.ModelSerializer):
    libro = LibroSerializer()
    region = RegionSerializer()
    ciudad = CiudadSerializer()
    comuna = ComunaSerializer()
    
    class Meta:
        model = Bodega
        fields = '__all__'
        
class UsuarioSerializer(serializers.ModelSerializer):
    region = RegionSerializer()
    comuna = ComunaSerializer()
    ciudad = CiudadSerializer()
    pais = PaisSerializer()
    
    class Meta:
        model = Usuario
        fields = '__all__'
        
class MovimientoSerializer(serializers.ModelSerializer):    
    libro = LibroSerializer()
    usuario = UsuarioSerializer()
    bodega = BodegaSerializer()
    
    class Meta:
        model = Movimiento
        fields = '__all__'