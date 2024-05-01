# estacionamiento
App estacionamiento - Python 3 - Nivel Intermedio UTN


https://github.com/ivanfortunesky/estacionamiento.git

********************************
En la Terminal

PS E:\Python>
PS E:\Python> git clone https://github.com/ivanfortunesky/estacionamiento.git
Cloning into 'estacionamiento'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.
PS E:\Python> cd .\estacionamiento\
PS E:\Python\estacionamiento>

****************************
BASH - 

895@Ivan-PC MINGW64 /e/Python
$ cd estacionamiento/

895@Ivan-PC MINGW64 /e/Python/estacionamiento (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean        

895@Ivan-PC MINGW64 /e/Python/estacionamiento (main)
$ python3 -m venv estacionamiento

895@Ivan-PC MINGW64 /e/Python/estacionamiento (main)
$ source estacionamiento/Scripts/activate
(estacionamiento) 
895@Ivan-PC MINGW64 /e/Python/estacionamiento (main)
$



1) Las clases deben nombrarse con mayúsculas, en lugar de "funciones" debería ser "Funciones".

Las clases deben iniciar con Mayúscula, por ejemplo:

class Abmc():

2) Si es un método de instancia no es un método estático, esto no esta bien:

    @staticmethod
    def actualizar_treeview(self, tree):

Para esta semana se propone presentar en el foro una aplicación que contenga:

3) Conexión y crud con base de datos sqlite3

4) Aplicación de patrón MVC

5) Programación Orientada a Objetos

Nota: El alumno que viene del nivel inicial puede partir de la app que realizo en ese nivel. Los que inician en este nivel pueden hacer una app nueva o tomar como punto de partida la que se les compartió en la unidad 1

Nota 2: La app puede ser realizada solo con python o mediante la incorporación de la interfaz gráfica tkinter

IMPORTANTE: No se pide como requisito hacer la app en pyqt


