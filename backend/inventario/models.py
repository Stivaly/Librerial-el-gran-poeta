from django.db import models

# Create your models here.
class Pais(models.Model):
    id_pais = models.AutoField(primary_key=True)
    pais = models.CharField(max_length=255)
    latitud = models.FloatField()
    longitud = models.FloatField()
    
    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'
        ordering = ['pais']

    def __str__(self):
        return self.nombre
    
class Autor(models.Model):
    id_autor = models.AutoField(primary_key=True)
    autor_genero = models.CharField(max_length=255)
    nombre_autor = models.CharField(max_length=255)
    autor_rating_promedio = models.FloatField()
    cantidad_rating_autor = models.IntegerField()
    cantidad_comentarios = models.IntegerField()
    id_pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre_autor']

    def __str__(self):
        return self.nombre_autor
    
class Editorial(models.Model):
    id_editorial = models.AutoField(primary_key=True)
    editorial = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = 'Editorial'
        verbose_name_plural = 'Editoriales'
        ordering = ['editorial']
    
    def __str__(self):
        return self.editorial
    
class Idioma(models.Model):
    id_idioma = models.AutoField(primary_key=True)
    idioma = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = 'Idioma'
        verbose_name_plural = 'Idiomas'
        ordering = ['idioma']
    
    def __str__(self) -> str:
        return self.idioma
    
class Genero(models.Model):
    id_genero = models.AutoField(primary_key=True)
    genero = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'
        ordering = ['genero']
    
class Libro(models.Model):
    id_libro = models.AutoField(primary_key=True)
    libro_nombre = models.CharField(max_length=255)
    libro_numpaginas = models.IntegerField()
    libro_rating_promedio = models.FloatField()
    libro_fecha_publicacion = models.DateField()
    id_editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    libro_review_counts = models.IntegerField()
    id_autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    id_idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE)
    libro_ISBN = models.CharField(max_length=255)
    id_genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['libro_nombre']
    
    def __str__(self) -> str:
        return self.libro_nombre
    
    
    def __str__(self) -> str:
        return self.genero
    
class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    region = models.CharField(max_length=255)
    id_pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regiones'
        ordering = ['region']
        
    def __str__(self) -> str:
        return self.region

class Ciudad(models.Model):
    id_ciudad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    id_region = models.ForeignKey(Region, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
        ordering = ['nombre']
        
    def __str__(self) -> str:
        return self.nombre
    
class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    id_region = models.ForeignKey(Region, on_delete=models.CASCADE)
    id_ciuad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Comuna'
        verbose_name_plural = 'Comunas'
        ordering = ['nombre']
        
    def __str__(self) -> str:
        return self.nombre
    
class Bodega(models.Model):
    id_bodega = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    calle = models.CharField(max_length=255)
    id_libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    id_region = models.ForeignKey(Region, on_delete=models.CASCADE)
    id_ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Bodega'
        verbose_name_plural = 'Bodegas'
        ordering = ['nombre']
        
    def __str__(self) -> str:
        return self.nombre 
    
class Usuario(models.Model):
    rut_usuario = models.IntegerField(primary_key=True) # Cambiar rut a char en bd
    codigo_verificador = models.CharField(max_length=1)
    nombre_usuario = models.CharField(max_length=255)
    correo = models.EmailField()
    contraseña = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    calle = models.CharField(max_length=255)
    id_region = models.ForeignKey(Region, on_delete=models.CASCADE)
    id_ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    id_pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['nombre_usuario']
        
    def __str__(self) -> str:
        return self.nombre_usuario
    
class Movimiento(models.Model):
    id_movimiento = models.AutoField(primary_key=True)
    id_libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    tipo_movimiento = models.CharField(max_length=255)
    cantidad = models.IntegerField()
    fecha = models.DateField()
    rut_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_bodega_origen = models.ForeignKey(Bodega, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Movimiento'
        verbose_name_plural = 'Movimientos'
        ordering = ['fecha']
        
    def __str__(self) -> str:
        return self.tipo_movimiento


        
        
    