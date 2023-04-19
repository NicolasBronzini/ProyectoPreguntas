import tkinter as tk
import conexion_db

class JuegoPreguntas(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Juego de Preguntas y Respuestas")
        
        # Configurar la conexión a la base de datos
        self.conexion = conexion_db.conectar()
        self.consulta = "SELECT pregunta, respuesta FROM tabla_de_preguntas"
        self.cursor = self.conexion.cursor()
        self.cursor.execute(self.consulta)
        self.preguntas_respuestas = self.cursor.fetchall()
        
        # Crear los widgets de la ventana
        self.label_pregunta = tk.Label(self.master, text="Pregunta:")
        self.label_pregunta.pack()
        self.entry_respuesta = tk.Entry(self.master)
        self.entry_respuesta.pack()
        self.boton_comprobar = tk.Button(self.master, text="Comprobar", command=self.comprobar_respuesta)
        self.boton_comprobar.pack()
        
        self.indice_pregunta = 0
        self.mostrar_pregunta_actual()

    def mostrar_pregunta_actual(self):
        pregunta, respuesta = self.preguntas_respuestas[self.indice_pregunta]
        self.label_pregunta.config(text=pregunta)
        self.entry_respuesta.delete(0, tk.END)
        
    def comprobar_respuesta(self):
        respuesta_usuario = self.entry_respuesta.get()
        _, respuesta_correcta = self.preguntas_respuestas[self.indice_pregunta]
        if respuesta_usuario == respuesta_correcta:
            tk.messagebox.showinfo("Respuesta Correcta", "¡Correcto!")
        else:
            tk.messagebox.showerror("Respuesta Incorrecta", f"Incorrecto. La respuesta correcta es: {respuesta_correcta}")
        self.indice_pregunta += 1
        if self.indice_pregunta >= len(self.preguntas_respuestas):
            tk.messagebox.showinfo("Fin del Juego", "Has completado todas las preguntas.")
            self.master.destroy()
        else:
            self.mostrar_pregunta_actual()

root = tk.Tk()
juego = JuegoPreguntas(root)
juego.pack()
root.mainloop()

# Cerrar la conexión a la base de datos
juego.conexion.close()
