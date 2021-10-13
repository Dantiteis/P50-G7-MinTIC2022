from AplicacionCiclo3.models.comentarios import Comentarios
from rest_framework import serializers
class ComentariosSerializers(serializers.ModelSerializer):
 class Meta:
    model = Comentarios
    fields = ['id','comentario']