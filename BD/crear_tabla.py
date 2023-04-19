from BD.conexion_db import conectar

# Crear la tabla "pregunta_respuesta"
def crear_tabla():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SHOW TABLES LIKE 'pregunta_respuesta'")
    result = cursor.fetchone()
    if result:
        print("La tabla ya existe")
    else:
        cursor.execute("CREATE TABLE pregunta_respuesta (id INT AUTO_INCREMENT PRIMARY KEY, enunciado VARCHAR(255), respuesta1 VARCHAR(255), respuesta2 VARCHAR(255), respuesta3 VARCHAR(255), respuesta4 VARCHAR(255), correcta INT)")
        print("Tabla creada")
    cursor.close()
    conexion.close()
