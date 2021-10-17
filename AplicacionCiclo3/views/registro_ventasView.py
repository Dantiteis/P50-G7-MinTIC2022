from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from AplicacionCiclo3.models import RegistroVentas
from AplicacionCiclo3.serializers import RegistroVentasSerializers


@api_view(['GET','POST'])
def registro_ventas_api_view(request):

    if request.method == 'GET':
        registroVentas = RegistroVentas.objects.all()
        registroVentas_serializer = RegistroVentasSerializers(registroVentas,many=True)
        return Response(registroVentas_serializer.data)
    elif request.method == 'POST':
        registro_ventas_serializer = RegistroVentasSerializers(data = request.data)
        if registro_ventas_serializer.is_valid():
            registro_ventas_serializer.save()
            return Response(registro_ventas_serializer.data)
        return Response(registro_ventas_serializer.errors)


'''Metodo para leer registro de ventas'''
@api_view(['GET'])
def registro_ventas_detail_view(request,pk=None):

    if request.method == 'GET':
        registroVentas = RegistroVentas.objects.filter(id = pk).first()
        registroVentas_serializer = RegistroVentasSerializers(registroVentas)
        return Response(registroVentas_serializer.data)   