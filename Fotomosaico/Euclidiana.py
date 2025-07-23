from dtabase import conexion, cursor 
import math 
import random

def buscar_color_mas_cercano(r_target, g_target, b_target, tabla):
      # Asegúrate de validar el nombre para evitar SQL injection
    query = f"""
        SELECT Name, R, G, B,   
            SQRT(POW(R - %s, 2) + POW(G - %s, 2) + POW(B - %s, 2)) AS distancia
        FROM {tabla}  
        ORDER BY distancia ASC    
        LIMIT 10;
    """

    #     query = """
    #     SELECT Name, R, G, B, 
    #            SQRT(POW(R - %s, 2) + POW(G - %s, 2) + POW(B - %s, 2)) AS distancia
    #     FROM promedio_rgb
    #     ORDER BY distancia ASC
    #     LIMIT 10;
    # """
    values = (r_target, g_target, b_target)
    
    cursor.execute(query, values)
    resultados = cursor.fetchall()  # Obtener los 10 resultados

    if resultados:
        resultado_aleatorio = random.choice(resultados)  # Elegir uno al azar
        return resultado_aleatorio
    else:
        print("No se encontró ningún color en la base de datos.")
        return None


def redondear_arriba(numero):
    if numero % 1 != 0:  # Si tiene parte decimal
        return math.ceil(numero)  # Redondea hacia arriba
    return int(numero)  # Si es un número entero, lo devuelve tal cual
