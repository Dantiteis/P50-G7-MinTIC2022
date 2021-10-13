from rest_framework import serializers
from AplicacionCiclo3.models.proveedores import Proveedores

class ProveedoresSerializers(serializers.ModelSerializer):
  class Meta:
    model = Proveedores
    fields = ['id','razon_social', 'correo_e', 'numero_telefono', 'direccion']