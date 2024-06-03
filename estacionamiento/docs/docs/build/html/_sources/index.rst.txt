Documentación de Estacionamiento
================================

**Estacionamiento** es una aplicación para gestionar el estacionamiento de vehículos, permitiendo agregar, modificar, eliminar y consultar registros de estacionamiento.

La aplicación está estructurada utilizando el patrón MVC (Modelo-Vista-Controlador).

.. note::

   Proyecto en construcción, correspondiente a la diplomatura de Python en la UTN 2024.


Modelo.py
==========================

El módulo `Modelo` proporciona la clase `Modelo` para gestionar los registros de estacionamiento en una base de datos SQLite.

Métodos
--------------------------

- ``__init__``: Inicializa el objeto `Modelo` y crea la conexión con la base de datos.
- ``conectar``: Establece una conexión con la base de datos SQLite.
- ``crear_tabla``: Crea una tabla en la base de datos si no existe.
- ``modificar``: Modifica un registro de una cochera en la base de datos.
- ``insertar_registro``: Inserta un nuevo registro de estacionamiento en la base de datos.
- ``consultar``: Recupera y muestra datos de la base de datos en el TreeView.
- ``borrar``: Elimina un registro de estacionamiento de la base de datos.
- ``validar_nombre``: Valida que el nombre y apellido ingresado sea alfanumérico.
- ``validar_telefono``: Valida que el teléfono ingresado contenga solo dígitos.
- ``validar_patente``: Valida que la patente ingresada esté en el formato correcto.


Vista.py
==========================

El módulo `Vista` define la interfaz gráfica de usuario de la aplicación de estacionamiento utilizando `tkinter`.

Métodos
--------------------------

- ``__init__``: Inicializa la interfaz gráfica de la aplicación.
- ``actualizar``: Actualiza los campos de entrada con la selección actual del TreeView.


Controlador.py
==========================

El módulo `Controlador` inicializa la aplicación de estacionamiento y gestiona la interacción entre la vista y el modelo.

Interfaz gráfica
==========================

.. image:: img/interfazgraficaestacionamiento.png
   :height: 300
   :width: 900
