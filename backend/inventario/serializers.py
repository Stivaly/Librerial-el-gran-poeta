from rest_framework import serializers
from django.contrib.auth.models import models
from .models import Pais, Autor, Editorial, Idioma, Libro, Genero, Region, Ciudad, Comuna, Bodega, Usuario, Movimiento, BodegaLibro

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = '__all__'
        
class AutorSerializer(serializers.ModelSerializer):
    pais = serializers.PrimaryKeyRelatedField(queryset=Pais.objects.all())
    
    class Meta:
        model = Autor
        fields = ['id_autor', 'nombre_autor', 'pais', 'autor_genero', 'autor_rating_promedio', 'cantidad_rating_autor', 'cantidad_comentarios']
        
class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = ['id_editorial', 'editorial']
        
class IdiomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idioma
        fields = '__all__'
        
        
class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'
        
class LibroSerializer(serializers.ModelSerializer):
    id_libro = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Libro
        fields = ['id_libro', 'libro_nombre', 'libro_numpaginas', 'libro_rating_promedio', 'libro_fecha_publicacion', 'libro_review_counts', 'libro_ISBN', 'id_editorial', 'id_autor', 'id_idioma', 'id_genero']
        
    def validate(self, data):
       
        required_fields = {
            'libro_nombre': "El nombre del libro es obligatorio.",
            'libro_numpaginas': "El número de páginas del libro es obligatorio.",
            'libro_fecha_publicacion': "La fecha de publicación del libro es obligatoria.",
            'libro_ISBN': "El ISBN del libro es obligatorio.",
            'id_editorial': "Debe seleccionar una editorial para el libro.",
            'id_autor': "Debe seleccionar un autor para el libro.",
            'id_idioma': "Debe seleccionar un idioma para el libro.",
            'id_genero': "Debe seleccionar un género para el libro."
        }

        for field, error_message in required_fields.items():
            if not data.get(field):
                raise serializers.ValidationError(error_message)

        return data
        
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
    
    class Meta:
        model = Bodega
        fields = ['id_bodega', 'nombre', 'calle', 'id_region', 'id_ciudad', 'id_comuna']
        
class UsuarioSerializer(serializers.ModelSerializer):
    region = RegionSerializer()
    comuna = ComunaSerializer()
    ciudad = CiudadSerializer()
    pais = PaisSerializer()
    
    class Meta:
        model = Usuario
        fields = '__all__'

class BodegaLibroSerializer(serializers.ModelSerializer):
    bodega = BodegaSerializer()
    libro = LibroSerializer()

    class Meta:
        model = BodegaLibro
        fields = ['bodega', 'libro', 'cantidad']
        
class MovimientoSerializer(serializers.ModelSerializer):    
    id_libro = serializers.PrimaryKeyRelatedField(queryset=Libro.objects.all())
    rut_usuario = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())
    id_bodega_origen = serializers.PrimaryKeyRelatedField(queryset=Bodega.objects.all(), allow_null=True, required=False)
    id_bodega_destino = serializers.PrimaryKeyRelatedField(queryset=Bodega.objects.all(), allow_null=True, required=False)
    
    class Meta:
        model = Movimiento
        fields = '__all__'
        
    def create(self, validated_data):
        # Crear el movimiento
        movimiento = Movimiento.objects.create(**validated_data)
        
        # Obtener o crear la entrada de BodegaLibro
        bodega_libro, created = BodegaLibro.objects.get_or_create(
            bodega=validated_data['id_bodega_origen'],
            libro=validated_data['id_libro']
        )
        
        # Actualizar la cantidad de libros en la bodega
        if movimiento.tipo_movimiento == 'entrada':
            bodega_libro.cantidad += movimiento.cantidad
        elif movimiento.tipo_movimiento == 'salida':
            bodega_libro.cantidad -= movimiento.cantidad
        elif movimiento.tipo_movimiento == 'traslado':
            bodega_libro.cantidad -= movimiento.cantidad
            bodega_destino, created = BodegaLibro.objects.get_or_create(
                bodega=validated_data['id_bodega_destino'],
                libro=validated_data['id_libro']
            )
            bodega_destino.cantidad += movimiento.cantidad
            bodega_destino.save()
        
        bodega_libro.save()

        return movimiento