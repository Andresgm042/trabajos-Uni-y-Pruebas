#esto es para recolectar imagenes y guardarlas
import cv2
import os
import time

nombre_carpeta = "dataset_galindo"

if not os.path.exists(nombre_carpeta):
    os.makedirs(nombre_carpeta)#si no existe la crea

cap = cv2.VideoCapture(0)

contador = 0
num_fotos = 50 #numero de fotos a tomar
intervalo = 1.3 #intervalo en segundos entre fotos

while contador < num_fotos:
    ret, frame = cap.read()
    if not ret or frame is None:
        print("Error en camara, a saber que")
        break

    ruta = f"{nombre_carpeta}/imagen_{contador}.jpg"

    cv2.imwrite(ruta, frame)

    cv2.imshow("Sonria mongolo", frame)
    print("Imagen guardada en {ruta}")

    contador += 1
    time.sleep(intervalo)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()