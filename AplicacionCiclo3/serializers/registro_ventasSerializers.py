from AplicacionCiclo3.models.registro_ventas import RegistroVentas
from rest_framework import serializers
class RegistroVentasSerializers(serializers.ModelSerializer):
 class Meta:
    model = RegistroVentas
    fields = [ 'id','idAdministrador','idCliente', 'idProducto', 'cantidad', 'fecha_venta']