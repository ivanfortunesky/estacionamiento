import sqlite3
import re
import os
from peewee import *
from tkinter.messagebox import showerror


modelo_path = os.path.dirname(os.path.abspath(__file__))
estacionamiento_db_path = os.path.join(modelo_path, "estacionamiento.db")

base = SqliteDatabase(estacionamiento_db_path) 


class ABMC: 
    def __init__(self): pass