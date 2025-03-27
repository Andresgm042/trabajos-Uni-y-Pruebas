import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Subir frame a la GPU
    gpu_frame = cv2.cuda_GpuMat()
    gpu_frame.upload(frame)

    # Convertir de BGR a HSV en GPU
    gpu_hsv = cv2.cuda.cvtColor(gpu_frame, cv2.COLOR_BGR2HSV)

    # Definir rango de color rojo en HSV
    lower_red = (0, 120, 70) #originalmente tenian que ser arrays de numpy
    upper_red = (10, 255, 255) #pero pues cuestiones de CUDA......

    # Aplicar filtro de color en GPU
    gpu_mask = cv2.cuda.inRange(gpu_hsv, lower_red, upper_red)

    # Convertir la máscara de 1 canal a 3 canales para hacer bitwise_and
    gpu_mask_color = cv2.cuda.cvtColor(gpu_mask, cv2.COLOR_GRAY2BGR)

    # Aplicar bitwise_and en GPU con la máscara corregida
    gpu_resultado = cv2.cuda.bitwise_and(gpu_frame, gpu_mask_color)

    # Descargar la imagen procesada para mostrarla en CPU
    resultado = gpu_resultado.download()

    # Mostrar el resultado
    cv2.imshow("Filtro de color (CUDA)", resultado)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
