# Generated by Django 4.2.13 on 2024-07-07 11:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitudes_Tolva',
            fields=[
                ('id_solicitudTolva', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tolva', models.CharField(max_length=100, verbose_name='Nombre del material')),
                ('fecha_realizarT', models.DateField(verbose_name='Fecha de Emisión')),
                ('descripcionTolva', models.CharField(max_length=300, verbose_name='Denominación - (Detalle correctamente los campos, como cantidad y descripción, es crucial para las solicitudes de tolva)')),
                ('tipo_retiro_pedido', models.CharField(choices=[('retirar compactadora', 'Retirar Compactadora'), ('retirar tolva de vidrio', 'Retirar Tolva de Vidrio'), ('retirar tolva abierta', 'Retirar Tolva Abierta'), ('pedir tolva abierta', 'Pedir Tolva Abierta'), ('pedir tolva grande', 'Pedir Tolva Grande'), ('pedir tolva mediana', 'Pedir Tolva Mediana'), ('pedir tolva pequeña', 'Pedir Tolva Pequeña')], max_length=100, verbose_name='Retiro o Pedidos de Tolva')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('tipo_usuario', models.CharField(choices=[('Trabajador', 'Trabajador'), ('Jefe', 'Jefe'), ('Administrador', 'Administrador')], max_length=30)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Solicitud de Tolva',
                'verbose_name_plural': 'Solicitudes de Tolvas',
            },
        ),
        migrations.CreateModel(
            name='Solicitudes_Retiro',
            fields=[
                ('id_solicitudRetiro', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_retiro', models.CharField(max_length=100, verbose_name='Material Retiro')),
                ('fecha_realizarR', models.DateField(verbose_name='Fecha de Emisión')),
                ('descripcionRetiro', models.CharField(max_length=300, verbose_name='Denominación - (Detalle correctamente los campos, como cantidad y descripción, es crucial para las solicitudes de retiro)')),
                ('cantidadRetiro', models.IntegerField(verbose_name='Cantidad a retirar')),
                ('tipo_materialRetiro', models.CharField(choices=[('fardo', 'Fardo'), ('kilo', 'Kilo'), ('bolsa', 'Bolsa'), ('un', 'UN')], max_length=10, verbose_name='Tipo de material de retiro')),
                ('patente', models.CharField(max_length=6, verbose_name='Patente del vehículo Ej:ABCD12')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('tipo_usuario', models.CharField(choices=[('Trabajador', 'Trabajador'), ('Jefe', 'Jefe'), ('Administrador', 'Administrador')], max_length=30)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Solicitud de retiro',
                'verbose_name_plural': 'Solicitudes de retiros',
            },
        ),
        migrations.CreateModel(
            name='Solicitudes_Epps',
            fields=[
                ('id_solicitudEpps', models.AutoField(primary_key=True, serialize=False)),
                ('nombreEpps', models.CharField(max_length=100, verbose_name='Nombre del EPP')),
                ('fecha_realizarEP', models.DateField(verbose_name='Fecha de Emisión')),
                ('descripcionEpps', models.CharField(max_length=300, verbose_name='Denominación - (Especifique adecuadamente talla y tipo de vestimenta para todos los EPPs)')),
                ('tipo_materialEpps', models.CharField(choices=[('unitario', 'Unitario'), ('más de un elemento', 'Más de un elemento')], max_length=300, verbose_name='Tipo de material de Epps')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('tipo_usuario', models.CharField(choices=[('Trabajador', 'Trabajador'), ('Jefe', 'Jefe'), ('Administrador', 'Administrador')], max_length=30)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Solicitud de EPP',
                'verbose_name_plural': 'Solicitudes de EPPs',
            },
        ),
    ]
