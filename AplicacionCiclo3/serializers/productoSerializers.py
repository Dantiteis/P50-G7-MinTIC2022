from rest_framework import serializers
from AplicacionCiclo3.models.producto import Producto

class ProductoSerializers(serializers.ModelSerializer):
    #id = serializers.RelatedField(source='idProducto', read_only=True)
    class Meta:
        model = Producto
        fields = ['id', 'modelo', 'tipo', 'entradas', 'salidas', 'pantalla_tamaño', 'pantalla_resolucion', 'bateria','software_incluido', 'tipo_disco', 'capacidad_disco', 'memoria_ram', 'procesador','precio']
