from tkinter import Tk
from tkinter import ttk
import vista_class

class Controlador:

    def __init__(self,raiz):
        try:
            self.controlador_raiz = raiz
            self.objeto_vista = vista_class.Vista(self.controlador_raiz)
        except Exception as error: 
            print(f"except dentro de def __init__(self,raiz): y se produjo el error {error}") 


if __name__ == "__main__":
    try:
        raiz = Tk()
        app = Controlador(raiz)
        raiz.mainloop()
    except Exception as error: 
        print(f"except dentro de if __name__ == __main__: y se produjo el error {error}")