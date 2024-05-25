from tkinter import Tk
from tkinter import ttk
import vista

class Controlador:

    def __init__(self,raiz):
        self.controlador_raiz = raiz
        self.objeto_vista = vista.Vista(self.controlador_raiz)
        


if __name__ == "__main__":
    raiz = Tk()
    app = Controlador(raiz)
    raiz.mainloop()
