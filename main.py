from tkinter import Tk
from BD.crear_tabla import crear_tabla
from interface.interfaz_grafica import InterfazGrafica

# Creacion de tabla en Db
crear_tabla()

# Interfaz gráfica
root = Tk()
app = InterfazGrafica(master=root)
app.mainloop()