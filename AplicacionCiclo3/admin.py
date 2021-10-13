from django.contrib import admin

from AplicacionCiclo3.models.comentarios import Comentarios
from .models.account import Account
from .models.cliente import Cliente
from .models.producto import Producto
from .models.proveedores import Proveedores
from .models.registro_ventas import RegistroVentas
from .models.comentarios import Comentarios
from .models.user import User

admin.site.register(User)
admin.site.register(Account)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Proveedores)
admin.site.register(RegistroVentas)
admin.site.register(Comentarios)

# Register your models here.
