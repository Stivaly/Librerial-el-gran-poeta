# Generated by Django 5.0.6 on 2024-07-04 10:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_alter_movimiento_fecha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bodega',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='bodega',
            name='id_libro',
        ),
        migrations.CreateModel(
            name='BodegaLibro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('bodega', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.bodega')),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.libro')),
            ],
            options={
                'verbose_name': 'Bodega Libro',
                'verbose_name_plural': 'Bodegas Libros',
                'unique_together': {('bodega', 'libro')},
            },
        ),
    ]
