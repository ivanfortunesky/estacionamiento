from tkinter import *
from tkinter import ttk
from modelo import *
#from modelo_peewee import *
#from modelo_class import Modelo


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
        Label(root, text="Nombre y Apellido").grid(row=3, column=0, sticky=W)
        Entry(root, textvariable=self.nombre).grid(row=3, column=1)
        Label(root, text="Teléfono").grid(row=4, column=0, sticky=W)
        Entry(root, textvariable=self.telefono).grid(row=4, column=1)


        # Botones
        Button(root, text="Ingresar Auto", command=lambda:insertar_registro(self.cochera,self.patente,self.nombre,self.telefono,self.tree)).grid(row=5, column=0)
        Button(root, text="Consultar", command=lambda:consultar(self.tree)).grid(row=5, column=1)
        Button(root, text="Borrar", command=lambda:borrar(self.tree)).grid(row=5, column=2)
        Button(root, text="Modificar", command=lambda:modificar(self.cochera,self.patente,self.nombre,self.telefono,self.tree)).grid(row=5, column=3)


        # TREEVIEW
        self.tree = ttk.Treeview(root, columns=("Cochera", "Patente", "Nombre", "Teléfono"), show="headings")
        self.tree.heading("Cochera", text="Cochera")
        self.tree.heading("Patente", text="Patente")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Teléfono", text="Teléfono")
        self.tree.grid(row=7, column=0, columnspan=4)


                ##################################################
        # Función para updatear las campos cuando selecciono un item
        self.tree.bind("<<TreeviewSelect>>", self.actualizar)   
    def actualizar(self,evento):
        selection = self.tree.selection()
        if selection: 
            cochera_seleccionada = self.tree.item(selection[0], "values")[0]  
            self.cochera.set(cochera_seleccionada)  # hago  la cochera para ahorrarme pasos al modificar
        if selection: 
            patente_seleccionada = self.tree.item(selection[0], "values")[1]  
            self.patente.set(patente_seleccionada)  # hago  la patente para ahorrarme clicks al modificar
        if selection: 
            nombre_seleccionada = self.tree.item(selection[0], "values")[2]  
            self.nombre.set(nombre_seleccionada)  # hago  el nombre para ahorrarme tipeo al modificar
        if selection: 
            telefono_seleccionada = self.tree.item(selection[0], "values")[3]  
            self.telefono.set(telefono_seleccionada)  # hago  el nombre para ahorrarme tipeo al modificar
        
        #self.tree.bind("<<TreeviewSelect>>", self.actualizar)
        ##################################################


        