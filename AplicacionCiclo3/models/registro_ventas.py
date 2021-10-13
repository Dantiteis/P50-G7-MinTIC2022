from django.db import models
from .cliente import Cliente
from datetime import datetime
from .user import User


class RegistroVentas(models.Model):
    id = models.AutoField(primary_key = True)
    idAdministrador = models.ForeignKey(User, related_name='registro_ventas', on_delete = models.CASCADE, null = True)
    idCliente = models.ForeignKey(Cliente, on_delete = models.CASCADE,null = True)
    fecha_venta = models.DateField(default=datetime.now) 