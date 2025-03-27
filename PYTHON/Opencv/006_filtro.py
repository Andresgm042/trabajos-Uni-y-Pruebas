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

    #se sube el frame a la GPU
    gpu_img = cv2.cuda_GpuMat()
    gpu_img.upload(frame_gray)

    #Se aplica canny en el frame de la GPU
    gpu_edges = gpu_canny.detect(gpu_img)
    #Se descarga el resultado a la CPU
    bordes = gpu_edges.download()

    #cv2.findContours(image, mode, method)
    contornos, _ = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 

    #Recorre cada contorno en la lista contornos y 
    #calcula su área. Si area es mayor a 500 píxeles, lo dibuja.
    for cnt in contornos:
        area = cv2.contourArea(cnt)
        if area > 200:
            #cv2.drawContours(image, contours, contourIdx, color, thickness)
            #Idx(indice, si es -1 dibuja todos los de la lista)
            #color en formato (B,R,G) - thickness(grosor, 2 pixels de grosor)
            cv2.drawContours(frame, [cnt], -1, (0,255,0), 2)

    #Se muestra
    cv2.imshow("Bordes en GPU", frame) #cambie edges por frame

     # Salir con la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()