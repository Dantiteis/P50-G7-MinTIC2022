from django.db import models
from .cliente import Cliente

class Comentarios(models.Model):
    id = models.AutoField(primary_key = True)
    idCliente = models.ForeignKey(Cliente, on_delete = models.CASCADE,null = True)
    comentario = models.CharField(max_length=300)