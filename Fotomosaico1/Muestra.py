from PIL import Image
import glob
import os 
from dtabase import conexion, cursor  # Importamos la conexión

# Buscar todas las imágenes .jpg en la carpeta "imagenes/"
rutas_imagenes = glob.glob("imagenes/*.jpg")

# Recorrer cada imagen
for ruta in rutas_imagenes:
    nombre = os.path.basename(ruta).split('.')[0]
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

    print(f"Imagen: {nombre} - Promedio RGB: ({rvalue}, {gvalue}, {bvalue})\n")

    # Insertar en la base de datos
    query = "INSERT INTO promedio_rgb (R, G, B, Name) VALUES (%s, %s, %s, %s);"
    values = (rvalue, gvalue, bvalue, nombre)

    try:
        cursor.execute(query, values)
        conexion.commit()  # Confirmar cambios
        print("Registro insertado con éxito")
    except Exception as e:
        print(f"Error al insertar en la base de datos: {e}")

# Cerrar conexión cuando termines
cursor.close()
conexion.close()


# from PIL import Image
# import glob
# from dtabase import *

# # Buscar todas las imágenes .jpg en la carpeta "imagenes/"
# rutas_imagenes = glob.glob("imagenes/*.jpg")  # Usa "imagenes/**/*.jpg" si hay subcarpetas

# # Recorrer cada imagen
# for ruta in rutas_imagenes:
#     imagen = Image.open(ruta).convert("RGB")  # Asegurar que la imagen esté en formato RGB
#     ancho, alto = imagen.size  # Obtener dimensiones
    
#     # Inicializar sumas de colores
#     rvalue, gvalue, bvalue = 0, 0, 0  

#     # Recorrer cada píxel de la imagen
#     pixelcount = 0
#     for y in range(alto):
#         for x in range(ancho):
#             r, g, b = imagen.getpixel((x, y))  # Obtener valores RGB
#             rvalue += r
#             gvalue += g
#             bvalue += b
#             pixelcount +=1
#     if pixelcount > 0:
#         rvalue /= pixelcount
#         gvalue /= pixelcount
#         bvalue /= pixelcount

#     print(rvalue)
#     print(gvalue)
#     print(bvalue)
#     print(" ")

#     query = ("INSERT INTO promedio_rgb (R, G, B) VALUES (%s, %s, %s);")
#     values = (rvalue, gvalue, bvalue)
#     try:
#         cursor.execute(query, values)
#         conexion.commit()  # Confirmar cambios
#         print("Registro insertado con éxito")
#     except Exception as e:
#         print(f"Error al insertar en la base de datos: {e}")


# print (rvalue/100)
# print(gvalue/100)
# print(bvalue/100)


# from PIL import Image

# # Cargar imagen
# imagen = Image.open("Ying.jpg").convert("RGB")

# # Inicializar sumas
# suma_r = 0
# suma_g = 0
# suma_b = 0

# # Recorrer los primeros 10x10 píxeles
# for y in range(10):
#     for x in range(10):
#         r, g, b = imagen.getpixel((x, y))
#         rvalue = +r
#         gvalue = +g
#         bvalue = +b
#         suma_r += r
#         suma_g += g
#         suma_b += b
#         print(f"Píxel ({x}, {y}): R={r}, G={g}, B={b}")

# # Imprimir resultados finales
# print(f"Suma total de R: {rvalue}")
# print(f"Suma total de G: {gvalue}")
# print(f"Suma total de B: {bvalue}")


