from django.db import models


class Producto(models.Model):
    id = models.IntegerField(primary_key = True)
    modelo     = models.CharField(max_length=20)
    tipo = models.CharField(max_length=50)
    entradas = models.CharField(max_length=20)
    salidas = models.CharField(max_length=30)
    pantalla_tamaño = models.CharField(max_length=30)
    pantalla_resolucion = models.CharField(max_length=30)
    pantalla_tamaño = models.CharField(max_length=30)
    bateria = models.CharField(max_length=30)
    software_incluido = models.BooleanField(default=False)
    tipo_disco = models.CharField(max_length=30)
    capacidad_disco = models.CharField(max_length=30)
    memoria_ram = models.CharField(max_length=30)
    procesador = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.modelo