from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from AplicacionCiclo3.models import Proveedores
from AplicacionCiclo3.serializers import ProveedoresSerializers

@api_view(['GET','POST'])
def proveedores_api_view(request):

    if request.method == 'GET':
        proveedores = Proveedores.objects.all()
        proveedores_serializer = ProveedoresSerializers(proveedores,many=True)
        return Response( proveedores_serializer.data)

    elif request.method == 'POST':
        proveedores_serializer = ProveedoresSerializers(data = request.data)
        if proveedores_serializer.is_valid():
            proveedores_serializer.save()
            return Response(proveedores_serializer.data)
        return Response(proveedores_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def proveedores_detail_view(request,pk=None):

    if request.method == 'GET':
        proveedores = Proveedores.objects.filter(id = pk).first()
        proveedores_serializer = ProveedoresSerializers(proveedores)
        return Response(proveedores_serializer.data)    
    elif request.method == 'PUT':
        proveedores = Proveedores.objects.filter(id = pk).first()
        proveedores_serializer = ProveedoresSerializers(data = request.data)
        if proveedores_serializer.is_valid():
            proveedores_serializer.save()
            return Response(proveedores_serializer.data)
        return Response(proveedores_serializer.errors)
    elif request.method == 'DELETE':
        proveedores = Proveedores.objects.filter(id = pk).first()
        proveedores.delete()
        return Response("El registro se eliminó correctamente.")

                            