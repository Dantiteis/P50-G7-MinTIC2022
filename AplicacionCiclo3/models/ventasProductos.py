from django.db import models
from .registro_ventas import RegistroVentas
from .producto import Producto

class VentasProductos(models.Model):
    idVentasProducto = models.AutoField(primary_key = True)
    idRegistroVentas = models.ForeignKey(RegistroVentas, on_delete = models.CASCADE)
    id = models.ForeignKey(Producto, on_delete = models.CASCADE)