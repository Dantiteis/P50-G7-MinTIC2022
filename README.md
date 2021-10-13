![header](doc/header.png)

# CONTROL ADMINISTRATIVO DE TIENDA DE COMPUTADORES

---

Authors:

- Lina Bocanegra
- Oscar Fabián Gomez
- Daniel Alejandro Rodríguez
- Julián Alberto Rosero
- Fabián S.

## TABLA DE CONTENIDO

---

1. [Descripción del problema](#Descripción)
2. [Organización del proyecto](#Organizacion)
3. [Como ejecutar la aplicacion](#eAplicacion)
4. [Licencia](#Licencia)
5. [Agradecimientos](#Agradecimientos)

## DESCRIPCIÓN DEL PROBLEMA

---

Una tienda de venta de computadores tiene exceso de información por manejar que requiere organizarse de modo óptimo, como los proveedores que posee, clientes frecuentes, histórico de ventas y productos disponibles para las ventas.

## ORGANIZACION DEL PROYECTO

---

El proyecto se encuentra conformado por la siguiente estructura de directorios y archivos (los más relevantes a la aplicación):

```
.
├── AplicacionCiclo3
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models
│   │   ├── account.py
│   │   ├── cliente.py
│   │   ├── comentarios.py
│   │   ├── __init__.py
│   │   ├── producto.py
│   │   ├── proveedores.py
│   │   ├── proveedorProducto.py
│   │   ├── registro_ventas.py
│   │   ├── user.py
│   │   └── ventasProductos.py
│   ├── serializers
│   │   ├── accountSerializers.py
│   │   ├── clienteSerializers.py
│   │   ├── comentariosSerializers.py
│   │   ├── __init__.py
│   │   ├── productoSerializers.py
│   │   ├── proveedoresSerializers.py
│   │   ├── registro_ventasSerializers.py
│   │   └── userSerializers.py
│   ├── tests.py
│   └── views
│       ├── __init__.py
│       ├── productoView.py
│       ├── proveedorView.py
│       ├── registro_ventasView.py
│       ├── userCreateView.py
│       └── userDetailView.py
├── Ciclo3Proyecto
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── requeriment.txt

```

## LICENCIA

Este proyecto se encuentra publicado bajo la licencia MIT. En [este enlace](https://opensource.org/licenses/MIT) podrá encontrar más información sobre la misma.
![footer](doc/footer.png)
