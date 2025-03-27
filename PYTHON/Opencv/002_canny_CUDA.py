import cv2 #libreria de opencv
import numpy as np

cap = cv2.VideoCapture(0) #abre camara

gpu_canny = cv2.cuda.createCannyEdgeDetector(100, 200)
while True:
    ret, frame = cap.read()
    if not ret:
        break

    #escala de grises
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #se sube a la GPU
    gpu_img = cv2.cuda_GpuMat()
    gpu_img.upload(frame_gray)

    #Se aplica canny en la GPU
    gpu_edges = gpu_canny.detect(gpu_img)
    #Se descarga el resultado a la CPU
    edges = gpu_edges.download()

    #Se muestra
    cv2.imshow("Bordes en GPU", edges)

     # Salir con la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()