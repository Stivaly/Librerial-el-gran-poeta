# Generated by Django 5.0.6 on 2024-06-30 06:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id_autor', models.AutoField(primary_key=True, serialize=False)),
                ('autor_genero', models.CharField(max_length=255)),
                ('nombre_autor', models.CharField(max_length=255)),
                ('autor_rating_promedio', models.FloatField()),
                ('cantidad_rating_autor', models.IntegerField()),
                ('cantidad_comentarios', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
                'ordering': ['nombre_autor'],
            },
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id_ciudad', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Ciudad',
                'verbose_name_plural': 'Ciudades',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id_editorial', models.AutoField(primary_key=True, serialize=False)),
                ('editorial', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Editorial',
                'verbose_name_plural': 'Editoriales',
                'ordering': ['editorial'],
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id_genero', models.AutoField(primary_key=True, serialize=False)),
                ('genero', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Genero',
                'verbose_name_plural': 'Generos',
                'ordering': ['genero'],
            },
        ),
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('id_idioma', models.AutoField(primary_key=True, serialize=False)),
                ('idioma', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Idioma',
                'verbose_name_plural': 'Idiomas',
                'ordering': ['idioma'],
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id_pais', models.AutoField(primary_key=True, serialize=False)),
                ('pais', models.CharField(max_length=255)),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
            ],
            options={
                'verbose_name': 'Pais',
                'verbose_name_plural': 'Paises',
                'ordering': ['pais'],
            },
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id_libro', models.AutoField(primary_key=True, serialize=False)),
                ('libro_nombre', models.CharField(max_length=255)),
                ('libro_numpaginas', models.IntegerField()),
                ('libro_rating_promedio', models.FloatField()),
                ('libro_fecha_publicacion', models.DateField()),
                ('libro_review_counts', models.IntegerField()),
                ('libro_ISBN', models.CharField(max_length=255)),
                ('id_autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.autor')),
                ('id_editorial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.editorial')),
                ('id_genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.genero')),
                ('id_idioma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.idioma')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
                'ordering': ['libro_nombre'],
            },
        ),
        migrations.AddField(
            model_name='autor',
            name='id_pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.pais'),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id_region', models.AutoField(primary_key=True, serialize=False)),
                ('region', models.CharField(max_length=255)),
                ('id_pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.pais')),
            ],
            options={
                'verbose_name': 'Region',
                'verbose_name_plural': 'Regiones',
                'ordering': ['region'],
            },
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id_comuna', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('id_ciuad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.ciudad')),
                ('id_region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.region')),
            ],
            options={
                'verbose_name': 'Comuna',
                'verbose_name_plural': 'Comunas',
                'ordering': ['nombre'],
            },
        ),
        migrations.AddField(
            model_name='ciudad',
            name='id_region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.region'),
        ),
        migrations.CreateModel(
            name='Bodega',
            fields=[
                ('id_bodega', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('calle', models.CharField(max_length=255)),
                ('cantidad', models.IntegerField()),
                ('id_ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.ciudad')),
                ('id_comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.comuna')),
                ('id_libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.libro')),
                ('id_region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.region')),
            ],
            options={
                'verbose_name': 'Bodega',
                'verbose_name_plural': 'Bodegas',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('rut_usuario', models.IntegerField(primary_key=True, serialize=False)),
                ('codigo_verificador', models.CharField(max_length=1)),
                ('nombre_usuario', models.CharField(max_length=255)),
                ('correo', models.EmailField(max_length=254)),
                ('contraseña', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=255)),
                ('calle', models.CharField(max_length=255)),
                ('id_ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.ciudad')),
                ('id_comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.comuna')),
                ('id_pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.pais')),
                ('id_region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.region')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'ordering': ['nombre_usuario'],
            },
        ),
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id_movimiento', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_movimiento', models.CharField(max_length=255)),
                ('cantidad', models.IntegerField()),
                ('fecha', models.DateField()),
                ('id_bodega_origen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.bodega')),
                ('id_libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.libro')),
                ('rut_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.usuario')),
            ],
            options={
                'verbose_name': 'Movimiento',
                'verbose_name_plural': 'Movimientos',
                'ordering': ['fecha'],
            },
        ),
    ]
