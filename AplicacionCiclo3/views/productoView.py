from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from AplicacionCiclo3.models import Producto
from AplicacionCiclo3.serializers import ProductoSerializers


@api_view(['GET','POST'])
def producto_api_view(request):

    if request.method == 'GET':
        producto = Producto.objects.all()
        producto_serializer = ProductoSerializers(producto,many=True)
        return Response(producto_serializer.data)
    elif request.method == 'POST':
        producto_serializer = ProductoSerializers(data = request.data)
        if producto_serializer.is_valid():
            producto_serializer.save()
            return Response(producto_serializer.data)
        return Response(producto_serializer.errors)

'''Metodo para leer, actualizar o borrar productos'''
@api_view(['GET','PUT','DELETE'])
def producto_detail_view(request,pk=None):

    if request.method == 'GET':
        producto = Producto.objects.filter(id = pk).first()
        producto_serializer = ProductoSerializers(producto)
        return Response(producto_serializer.data)    
    elif request.method == 'PUT':
        producto = Producto.objects.filter(id = pk).first()
        producto_serializer = ProductoSerializers(instance = producto, data = request.data)
        if producto_serializer.is_valid():
            producto_serializer.save()
            return Response(producto_serializer.data)
        return Response(producto_serializer.errors)
    elif request.method == 'DELETE':
        producto = Producto.objects.filter(id = pk).first()
        producto.delete()
        return Response("El producto ha sido eliminado de manera exitosa..")