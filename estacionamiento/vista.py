from tkinter import *
from tkinter import ttk
import modelo

class Vista:
    def __init__(self, root):
        self.root = root
        self.root.title("Estacionamiento")

        self.cochera = StringVar()
        self.patente = StringVar()
        self.nombre = StringVar()
        self.telefono = StringVar()

        # Etiquetas y entradas
        Label(root, text="Cochera").grid(row=1, column=0, sticky=W)
        Entry(root, textvariable=self.cochera).grid(row=1, column=1)
        Label(root, text="Patente").grid(row=2, column=0, sticky=W)
        Entry(root, textvariable=self.patente).grid(row=2, column=1)
        Label(root, text="Nombre").grid(row=3, column=0, sticky=W)
        Entry(root, textvariable=self.nombre).grid(row=3, column=1)
        Label(root, text="Teléfono").grid(row=4, column=0, sticky=W)
        Entry(root, textvariable=self.telefono).grid(row=4, column=1)

        # Botones
        Button(root, text="Ingresar Auto", command=modelo.insertar_registro).grid(row=5, column=0)
        Button(root, text="Consultar", command=modelo.consultar).grid(row=5, column=1)
        Button(root, text="Borrar", command=modelo.borrar).grid(row=5, column=2)
        Button(root, text="Modificar", command=modelo.modificar).grid(row=5, column=3)

        # TREEVIEW
        self.tree = ttk.Treeview(root, columns=("Cochera", "Patente", "Nombre", "Teléfono"), show="headings")
        self.tree.heading("Cochera", text="Cochera")
        self.tree.heading("Patente", text="Patente")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Teléfono", text="Teléfono")
        self.tree.grid(row=7, column=0, columnspan=4)

                ##################################################
        # Función para updatear las campos cuando selecciono un item
        tree.bind("<<TreeviewSelect>>", actualizar)
        
        def actualizar(evento):
            selection = tree.selection()
            if selection: 
                cochera_seleccionada = tree.item(selection[0], "values")[0]  
                cochera.set(cochera_seleccionada)  # hago  la cochera para ahorrarme pasos al modificar
            if selection: 
                patente_seleccionada = tree.item(selection[0], "values")[1]  
                patente.set(patente_seleccionada)  # hago  la patente para ahorrarme clicks al modificar
            if selection: 
                nombre_seleccionada = tree.item(selection[0], "values")[2]  
                nombre.set(nombre_seleccionada)  # hago  el nombre para ahorrarme tipeo al modificar
            if selection: 
                telefono_seleccionada = tree.item(selection[0], "values")[3]  
                telefono.set(telefono_seleccionada)  # hago  el nombre para ahorrarme tipeo al modificar
        
            
        ##################################################


        