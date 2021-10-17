from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from AplicacionCiclo3.models import Cliente
from AplicacionCiclo3.serializers import ClienteSerializer


@api_view(['GET','POST'])
def cliente_api_view(request):

    if request.method == 'GET':
        cliente = Cliente.objects.all()
        cliente_serializer = ClienteSerializer(cliente,many=True)
        return Response(cliente_serializer.data)
    elif request.method == 'POST':
        cliente_serializer = ClienteSerializer(data = request.data)
        if cliente_serializer.is_valid():
            cliente_serializer.save()
            return Response(cliente_serializer.data)
        return Response(cliente_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def cliente_detail_view(request,pk=None):

    if request.method == 'GET':
        cliente = Cliente.objects.filter(id = pk).first()
        cliente_serializer = ClienteSerializer(cliente)
        return Response(cliente_serializer.data)    
    elif request.method == 'PUT':
        cliente = Cliente.objects.filter(id = pk).first()
        cliente_serializer = ClienteSerializer(data = request.data)
        if cliente_serializer.is_valid():
            cliente_serializer.save()
            return Response(cliente_serializer.data)
        return Response(cliente_serializer.errors)
    elif request.method == 'DELETE':
        cliente = Cliente.objects.filter(id = pk).first()
        cliente.delete()
        return Response("El cliente fue eliminado")