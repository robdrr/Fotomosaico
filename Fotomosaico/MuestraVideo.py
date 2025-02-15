import cv2
import os

def extraer_fotogramas(video_path, output_folder):
    # Crear la carpeta de salida si no existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Capturar el video
    cap = cv2.VideoCapture(video_path)

    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()  # Leer fotograma
        if not ret:
            break  # Si no hay más fotogramas, salir

        # Guardar el fotograma como imagen JPG
        frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_filename, frame)

        frame_count += 1

    cap.release()
    cv2.destroyAllWindows()
    print(f"Se han guardado {frame_count} fotogramas en '{output_folder}'.")

# Uso de la función
video_path = "videos/PichaAwards2024.mp4"  # Ruta del video de entrada
output_folder = "videos/fotogramas"  # Carpeta donde se guardarán los fotogramas
extraer_fotogramas(video_path, output_folder)
