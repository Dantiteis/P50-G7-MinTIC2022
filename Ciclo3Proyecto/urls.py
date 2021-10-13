"""Ciclo3Proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from AplicacionCiclo3 import views
from AplicacionCiclo3.views.productoView import producto_api_view, producto_detail_view
from AplicacionCiclo3.views.proveedorView import proveedores_api_view, proveedores_detail_view
from AplicacionCiclo3.views.registro_ventasView import registro_ventas_api_view, registro_ventas_detail_view
from AplicacionCiclo3.views.comentariosView import comentarios_api_view#, comentarios_detail_view

from AplicacionCiclo3.views.clienteView import cliente_api_view, cliente_detail_view


urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.UserCreateView.as_view(), name='User'),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    path('producto/', views.producto_api_view),
    path('producto/<int:pk>', views.producto_detail_view),
    path('proveedores/',views.proveedores_api_view, name='Proveedores'),
    path('proveedores/<int:pk>',views.proveedores_detail_view),
    path('registro_ventas/',views.registro_ventas_api_view, name='RegistroVentas'),
    path('registro_ventas/<int:pk>',views.registro_ventas_detail_view),
    path('comentarios/',views.comentarios_api_view, name='Comentarios'),
    path('comentarios/<int:pk>',views.comentarios_detail_view),
    path('cliente/', views.cliente_api_view),
    path('cliente/<int:pk>', views.cliente_detail_view),
]