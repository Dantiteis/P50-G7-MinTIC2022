from django.db import models
from .proveedores import Proveedores
from .producto import Producto

class ProveedorProductos(models.Model):
    #idVentasProducto
    idVentasProducto = models.AutoField(primary_key = True)
    #idProveedores
    id= models.ForeignKey(Proveedores, on_delete = models.CASCADE)
    #idProducto
    id = models.ForeignKey(Producto, on_delete = models.CASCADE)