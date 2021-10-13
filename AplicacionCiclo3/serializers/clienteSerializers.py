from rest_framework import serializers
from AplicacionCiclo3.models.cliente import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'name', 'surname', 'phone', 'email','direccion']