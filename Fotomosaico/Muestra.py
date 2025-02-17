from PIL import Image
import glob
import os 
from dtabase import conexion, cursor  # Importamos la conexión

# Buscar todas las imágenes .jpg en la carpeta "imagenes/"
import glob

# Buscar todas las imágenes .jpg en "imagenes/" y sus subcarpetas
rutas_imagenes = glob.glob("imagenes/paisajes/*.jpg", recursive=True)

# Recorrer cada imagen
for ruta in rutas_imagenes:
    # nombre = os.path.basename(ruta).split('.')[0]
    nombre_archivo = os.path.basename(ruta)
    nombre_carpeta = os.path.basename(os.path.dirname(ruta))
    nombre_completo = f"{nombre_carpeta}/{nombre_archivo}"
    imagen = Image.open(ruta).convert("RGB")
    ancho, alto = imagen.size  

    # Inicializar sumas de colores
    rvalue, gvalue, bvalue = 0, 0, 0  
    pixelcount = 0

    # Recorrer cada píxel de la imagen
    for y in range(alto):
        for x in range(ancho):
            r, g, b = imagen.getpixel((x, y))  
            rvalue += r
            gvalue += g
            bvalue += b
            pixelcount += 1

    if pixelcount > 0:
        rvalue /= pixelcount
        gvalue /= pixelcount
        bvalue /= pixelcount

    # print(f"Imagen: {nombre_completo} - Promedio RGB: ({rvalue}, {gvalue}, {bvalue})\n")

    # Insertar en la base de datos
    query = "INSERT INTO paisajes_rgb (R, G, B, Name) VALUES (%s, %s, %s, %s);"
    values = (rvalue, gvalue, bvalue, nombre_completo)

    try:
        cursor.execute(query, values)
        conexion.commit()  # Confirmar cambios
        # print("Registro insertado con éxito")
    except Exception as e:
        print(f"Error al insertar en la base de datos: {e}")

print("Termino de ejecutar")
# Cerrar conexión cuando termines
cursor.close()
conexion.close()

