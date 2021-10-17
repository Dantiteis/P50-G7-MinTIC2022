from django.db import models


class Proveedores(models.Model):
    id= models.IntegerField(primary_key = True)
    razon_social = models.CharField(max_length=30)
    correo_e     = models.EmailField()
    numero_telefono = models.CharField(max_length = 30)
    direccion = models.CharField(max_length = 30)

    def __str__(self) -> str:
        return self.razon_social