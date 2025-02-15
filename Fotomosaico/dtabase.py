import mysql.connector

# Conectar a MySQL y la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ford2007.",
    database="RGB_FOTOS"  # Asegurar que usamos la base de datos correcta
)

cursor = conexion.cursor()

# Crear la tabla si no existe
cursor.execute("""
    CREATE TABLE IF NOT EXISTS avg_rgb (
        id INT AUTO_INCREMENT PRIMARY KEY,
        R FLOAT NOT NULL,
        G FLOAT NOT NULL,
        B FLOAT NOT NULL,
        Name VARCHAR(50) UNIQUE NOT NULL
    )
""")
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS promedio_rgb (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         R FLOAT NOT NULL,
#         G FLOAT NOT NULL,
#         B FLOAT NOT NULL,
#         Name VARCHAR(50) UNIQUE NOT NULL
#     )
# """)

conexion.commit()
cursor.close()
conexion.close()

# print("Tabla 'promedio_rgb' creada exitosamente.")


def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ford2007.",
        database="RGB_FOTOS"
    )

# Conexión global
conexion = conectar()
cursor = conexion.cursor()