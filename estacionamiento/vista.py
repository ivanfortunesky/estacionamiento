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


        root.mainloop()