import tkinter as tk

class InterfazGrafica(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.crear_widgets()

    def crear_widgets(self):
        self.etiqueta = tk.Label(self, text="¡Bienvenido al Juego!")
        self.etiqueta.pack(side="top")

        self.boton_jugar = tk.Button(self, text="Jugar", fg="green",
                                     command=self.abrir_juego)
        self.boton_jugar.pack(side="left")

        self.boton_salir = tk.Button(self, text="Salir", fg="red",
                                     command=self.master.destroy)
        self.boton_salir.pack(side="right")

    def abrir_juego(self):
        # Aquí puedes llamar a la función que abre el juego
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazGrafica(master=root)
    app.mainloop()
