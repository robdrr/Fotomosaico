from dtabase import conexion, cursor  
def buscar_color_mas_cercano(r_target, g_target, b_target):
    query = """
        SELECT Name, R, G, B, 
               SQRT(POW(R - %s, 2) + POW(G - %s, 2) + POW(B - %s, 2)) AS distancia
        FROM promedio_rgb
        ORDER BY distancia ASC
        LIMIT 1;
    """
    values = (r_target, g_target, b_target)
    
    cursor.execute(query, values)
    resultado = cursor.fetchone()

    if resultado:
        # nombre, R, G, B, distancia = resultado
        # print(f"Color más cercano: {nombre} (R: {R}, G: {G}, B: {B}) - Distancia: {distancia}")
        return resultado
    else:
        print("No se encontró ningún color en la base de datos.")
        return None