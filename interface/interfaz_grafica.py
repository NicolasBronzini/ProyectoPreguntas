import tkinter as tk

class InterfazGrafica(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.crear_widgets()

    def crear_widgets(self):
        self.etiqueta = tk.Label(self, text="Hola, esta es una interfaz gráfica básica.")
        self.etiqueta.pack(side="top")

        self.boton = tk.Button(self, text="Salir", fg="red",
                              command=self.master.destroy)
        self.boton.pack(side="bottom")

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazGrafica(master=root)
    app.mainloop()
