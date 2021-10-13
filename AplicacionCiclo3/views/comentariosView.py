from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from AplicacionCiclo3.models import Comentarios
from AplicacionCiclo3.serializers import ComentariosSerializers


@api_view(['GET','POST'])
def comentarios_api_view(request):

    if request.method == 'GET':
        comentarios = Comentarios.objects.all()
        comentarios_serializer = ComentariosSerializers(comentarios,many=True)
        return Response(comentarios_serializer.data)
    
    elif request.method == 'POST':
            comentarios_serializer = ComentariosSerializers(data=request.data)
                          
            if  comentarios_serializer.is_valid():
                comentarios_serializer.save()
                return Response( comentarios_serializer.data)
            return Response( comentarios_serializer.errors)

'''Metodo para leer Comentarios'''
@api_view(['GET'])
def comentarios_detail_view(request,pk=None):

    if request.method == 'GET':
        comentarios = Comentarios.objects.filter(id = pk).first()
        comentarios_serializer = ComentariosSerializers(comentarios)
        return Response(comentarios_serializer.data)
