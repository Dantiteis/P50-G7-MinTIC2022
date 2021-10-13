from django.db import models

class Cliente(models.Model):
    id = models.BigAutoField(primary_key=True),
    name  = models.CharField(max_length=20)
    surname   = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    direccion = models.CharField(max_length=30)
  
    def __str__(self) -> str:
        return self.name