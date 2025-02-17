from PIL import Image
from Euclidiana import *

Photo = "Generar/Prueba1.jpg"
imagen = Image.open(Photo).convert("RGB")
avg = []
ancho, alto = imagen.size
tamanhofoto = 10  # Tamaño de cada bloque
tabla = "paisajes_rgb"
# Recorrer la imagen en bloques de tamanhofoto × tamanhofoto
for y in range(0, alto, tamanhofoto):
    quoe = []
    for x in range(0, ancho, tamanhofoto):
        rvalue = gvalue = bvalue = pixelcount = 0
        
        # Recorrer cada píxel dentro del bloque actual
        for i in range(tamanhofoto):
            for j in range(tamanhofoto):
                if (x + j) < ancho and (y + i) < alto:  # Verifica que esté dentro de la imagen
                    r, g, b = imagen.getpixel((x + j, y + i))
                    rvalue += r
                    gvalue += g
                    bvalue += b
                    pixelcount += 1
        
        if pixelcount > 0:  # Evitar división por cero
            rvalue /= pixelcount
            gvalue /= pixelcount
            bvalue /= pixelcount 

        quoe.append((rvalue, gvalue, bvalue))
    avg.append(quoe)

# Cargar imagen base para pegar los mosaicos
img_base = Image.open(Photo)

# Calcular número de bloques por fila y columna
fila = (ancho + tamanhofoto - 1) // tamanhofoto  # Redondeo hacia arriba
columna = (alto + tamanhofoto - 1) // tamanhofoto
print("paso 1")
# Reemplazar bloques con imágenes más cercanas
for a in range(columna):
    for be in range(fila):
        if a < len(avg) and be < len(avg[a]):  # Evitar errores de índice
            rsearch, gsearch, bsearch = avg[a][be]
            name, r, g, b, distancia = buscar_color_mas_cercano(rsearch, gsearch, bsearch, tabla)
            
            img_insert = Image.open(f'imagenes/{name}')
            img_resized = img_insert.resize((tamanhofoto, tamanhofoto))
            
            posicion = (int(be * tamanhofoto), int(a * tamanhofoto))
            
            if img_insert.mode == "RGBA":
                img_base.paste(img_resized, posicion, img_resized)
            else:
                img_base.paste(img_resized, posicion)

img_base.save("resultado12.jpg") 
img_base.show()



        






