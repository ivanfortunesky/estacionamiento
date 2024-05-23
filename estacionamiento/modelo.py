import sqlite3
import re
import os
import peewee
from tkinter.messagebox import showerror

def conectar():
     try:
        modelo_path = os.path.dirname(os.path.abspath(__file__))
        estacionamiento_db_path = os.path.join(modelo_path, "estacionamiento.db")
        print("Path a la base de datos: ",estacionamiento_db_path)
        con = sqlite3.connect(estacionamiento_db_path)
        return con
     except Exception as error: 
         print(f"except dentro de conectar y se produjo el error {error}")

def crear_tabla():
    try:
        con = conectar()
        cursor = con.cursor()
        print("Estoy dentro de crear_tabla()")
        cursor.execute('''CREATE TABLE IF NOT EXISTS estacionamiento (
                        id INTEGER PRIMARY KEY,
                        cochera INTEGER,
                        patente TEXT, 
                        nombre TEXT,
                        telefono TEXT)''')
        con.commit()
        con.close()
    except Exception as error: 
        print(f"except dentro de crear_tabla y se produjo el error {error}")
# Crear tabla si no existe
crear_tabla()
########################################################
########################################################
    
#Función para modificar un registro de una cochera, por ejemplo cambirle la patente
    
########################################################
########################################################
    
def modificar(cochera,patente,nombre,telefono,tree):
    try:
        selection = tree.selection()
        if not selection:
            showerror("Error", "seleccione el registro a Modificar")
            return
        #cochera.set(tree.item(selection[0], "values")[0])

        cochera_local = cochera.get()
        patente_local  = validar_patente(patente.get())
        nombre_local  = validar_nombre(nombre.get())
        telefono_local  = validar_telefono(telefono.get())
    
            
        
        # Validar que todos los campos estén llenos
        if patente_local == "" or nombre_local == "" or telefono_local == "":
            showerror("Error", "Por favor, complete todos los campos.")
            return
        
        # Validar que el teléfono contenga solo dígitos
        if not telefono_local.isdigit():
            showerror("Error", "El teléfono debe contener solo números.")
            return
        
        # Conectar a la base de datos
        con = conectar()
        cursor = con.cursor()

        # updatear la base con los nuevos valores para ese registro

        cursor.execute('''UPDATE estacionamiento 
                        SET patente = ?, nombre = ?, telefono = ?
                        WHERE cochera = ?''',
                    (patente_local, nombre_local, telefono_local, cochera_local))
        con.commit()
        con.close()
        # Refrescar la tabla mostrada en treeview
        consultar(tree)
        print(f"Estoy dentro de modificar y se modificó el registro de la cochera N# {cochera_local}")
    except Exception as error: 
        print(f"except dentro de modificar y se produjo el error {error}")



########################################################
########################################################

# Función para insertar un nuevo registro
def insertar_registro(cochera,patente,nombre,telefono,tree):
    try:    
        cochera_local = cochera.get()
        patente_local  = validar_patente(patente.get())
        #Validar con REGEX (nombre, telefono y patente)
        nombre_local  = validar_nombre(nombre.get())
        telefono_local  = validar_telefono(telefono.get())
        
        # Validar que todos los campos estén llenos
        if cochera_local == "" or patente_local == "" or nombre_local == "" or telefono_local == "":
            showerror("Error", "Por favor, complete todos los campos.")
            return   
        
        # Validar que el teléfono contenga solo dígitos
        """if not telefono_local.isdigit():
            showerror("Error", "El teléfono debe contener solo números.")
            return
        """
        # Conectar a la base de datos
        con = conectar()
        cursor = con.cursor()
        
        # Verificar si la cochera está ocupada
        cursor.execute('''SELECT * FROM estacionamiento WHERE cochera = ?''', (cochera_local,))
        if cursor.fetchone():
            showerror("Error", f"La cochera {cochera_local} ya está ocupada.")
            return
        
        # Insertar el registro
        cursor.execute('''INSERT INTO estacionamiento (cochera, patente, nombre, telefono) VALUES (?, ?, ?, ?)''', (cochera_local, patente_local, nombre_local, telefono_local))
        con.commit()
        con.close()
        
        #showinfo("Información", "Registro insertado correctamente.")
        consultar(tree)
    except Exception as error: 
        print(f"except dentro de insertar_registro y se produjo el error {error}")

# Función para consultar registros
def consultar(tree):
    try:
        # Limpiar el Treeview antes de agregar nuevos datos
        for row in tree.get_children():
            tree.delete(row)
        
        con = conectar()
        cursor = con.cursor()
        cursor.execute('''SELECT * FROM estacionamiento''') # traigo de la base estacionamiento TODO
        filas = cursor.fetchall()
        con.close()
        filas_ordenadas = sorted(filas, key=lambda x: x[1])
        for fila in filas_ordenadas:
            tree.insert("", "end", values=(fila[1], fila[2], fila[3], fila[4]))
    except Exception as error: 
        print(f"except dentro de consultar(tree) y se produjo el error {error}")

    
# Función para borrar una reserva
def borrar(tree):
    try:
        selection = tree.selection()
        if not selection:
            showerror("Error", "seleccione un registro para borrar.")
            return
        
        con = conectar()
        cursor = con.cursor()
        for item in selection:
            cursor.execute('''DELETE FROM estacionamiento WHERE cochera = ?''', (tree.item(item, "values")[0],))
        con.commit()
        con.close()
        
        #showinfo("Información", "Se borró el registro de esa cochera")
        consultar(tree)
    except Exception as error: 
        print(f"except dentro de borrar(tree) y se produjo el error {error}")


##################################################
#Función validar con Regex (Nombre solo alfanumerico y telefono solo dígitos sín espacios)

def validar_nombre(expresion_a_validar):
        try:
            nombre_regex = re.compile(r"^[A-Za-záéíóúñ]{2,}([\s][A-Za-záéíóúñ]{2,})+$", re.I)
                
            if nombre_regex.match(expresion_a_validar):
                return expresion_a_validar.title()
            else: 
                showerror("Error", "Completar Nombre y Apellido, solo alfanumerico.")
                return "<ERR formato Nom>"
        except Exception as error: 
            print(f"except dentro de validar_nombre(expresion_a_validar) y se produjo el error {error}")

def validar_telefono(expresion_a_validar):
        try:
            telefono_regex = re.compile(r"[0-9]{8,}$")
            
            if telefono_regex.match(expresion_a_validar):
                return expresion_a_validar
            else: 
                showerror("Error", "Completar telefono completo, solo números.")
                return "<ERR formato Tel>"
        except Exception as error: 
            print(f"except dentro de validar_telefono(expresion_a_validar) y se produjo el error {error}")

def validar_patente(expresion_a_validar):
    try:
        return expresion_a_validar.upper()
    except Exception as error: 
        print(f"except dentro de validar_patente(expresion_a_validar) y se produjo el error {error}")
        
##################################################  