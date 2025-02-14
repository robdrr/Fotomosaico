from PIL import Image
import math

from pprint import pprint
from dtabase import conexion, cursor  

from Euclidiana import *
Photo = "imagenes/imagenBW.jpg"
imagen = Image.open(Photo).convert("RGB")
avg = []
ancho, alto = imagen.size
tamanhofoto = 100
for y in range(0, alto, tamanhofoto):
    quoe = []
    for x in range(0, ancho, tamanhofoto):
        rvalue = 0
        gvalue = 0
        bvalue = 0
        pixelcount = 0
        for i in range(tamanhofoto):
            for j in range(tamanhofoto):
                if (x + j) < ancho and (y + i) < alto:
                    r, g, b = imagen.getpixel((j+x, i+y))
                    rvalue += r
                    gvalue += g
                    bvalue += b
                    pixelcount +=1
        if pixelcount > 0:
            rvalue /= pixelcount
            gvalue /= pixelcount
            bvalue /= pixelcount 

        quoe.append((rvalue, gvalue, bvalue))
    avg.append(quoe)

def redondear_arriba(numero):
    if numero % 1 != 0:  # Si tiene parte decimal
        return math.ceil(numero)  # Redondea hacia arriba
    return int(numero)  # Si es un número entero, lo devuelve tal cual



# for a in range()

fila = redondear_arriba(ancho/tamanhofoto)
columna = redondear_arriba(alto/tamanhofoto)
name = ''
for a in range(columna):
    for b in range(fila):
        rsearch, gsearch, bsearch = avg[a][b]
        name, r, g, b, distancia =buscar_color_mas_cercano(rsearch, gsearch, bsearch)
        img_base= Image.open(Photo)
        img_insert = Image.open(f'imagenes/{name}.jpg')






