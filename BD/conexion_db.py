import mysql.connector

def conectar():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="preguntas_respuestas"
    )
    return conexion
