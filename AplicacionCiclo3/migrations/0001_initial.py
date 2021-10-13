# Generated by Django 3.2.8 on 2021-10-13 15:16

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('direccion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('modelo', models.CharField(max_length=20)),
                ('tipo', models.CharField(max_length=50)),
                ('entradas', models.CharField(max_length=20)),
                ('salidas', models.CharField(max_length=30)),
                ('pantalla_resolucion', models.CharField(max_length=30)),
                ('pantalla_tamaño', models.CharField(max_length=30)),
                ('bateria', models.CharField(max_length=30)),
                ('software_incluido', models.BooleanField(default=False)),
                ('tipo_disco', models.CharField(max_length=30)),
                ('capacidad_disco', models.CharField(max_length=30)),
                ('memoria_ram', models.CharField(max_length=30)),
                ('procesador', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('razon_social', models.CharField(max_length=30)),
                ('correo_e', models.EmailField(max_length=254)),
                ('numero_telefono', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='RegistroVentas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_venta', models.DateField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VentasProductos',
            fields=[
                ('idVentasProducto', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AplicacionCiclo3.producto')),
                ('idRegistroVentas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AplicacionCiclo3.registroventas')),
            ],
        ),
        migrations.AddField(
            model_name='registroventas',
            name='idAdministrador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='registro_ventas', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='registroventas',
            name='idCliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AplicacionCiclo3.cliente'),
        ),
        migrations.CreateModel(
            name='ProveedorProductos',
            fields=[
                ('idVentasProducto', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AplicacionCiclo3.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('comentario', models.CharField(max_length=300)),
                ('idCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AplicacionCiclo3.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('balance', models.IntegerField(default=0)),
                ('lastChangeDate', models.DateTimeField()),
                ('isActive', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
