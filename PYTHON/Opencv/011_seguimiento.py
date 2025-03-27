import cv2
import numpy as np

cap = cv2.VideoCapture(0)
trayectoria = [] #una lista vacia para guardar la trayectoria del objeto

while True:

    ret, frame = cap.read()
    if not ret:
        break

    gpu_frame = cv2.cuda_GpuMat()
    gpu_frame.upload(frame)

    gpu_hsv = cv2.cuda.cvtColor(gpu_frame, cv2.COLOR_BGR2HSV)

    lower_blue = (100, 120, 70)
    upper_blue = (140, 255, 255)

    gpu_mask = cv2.cuda.inRange(gpu_hsv, lower_blue, upper_blue)
    mask = gpu_mask.download()

    #cv2.findContours(image, mode, method)
    contornos, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contornos:
        area = cv2.contourArea(cnt)
        if area > 400:
            #moments es un diccionario que contiene información sobre el contorno
            #como el área, el centroide, el perímetro, etc.
            moments = cv2.moments(cnt)
            #["m00"] área del contorno, ["m10"] y ["m01"] Se usan para calcular el centroide.

            if moments["m00"] != 0: #si area de contorno es diferente a 0
                cx = int(moments["m10"] / moments["m00"])#coordenada x del centroide
                cy = int(moments["m01"] / moments["m00"])#coordenada y del centroide
                trayectoria.append((cx, cy))  # Guardar trayectoria
                
                 # Dibujar círculo en el centro del objeto
                 #cv2.circle(imagen, coordinadas del centro, radius, color, grosor)
                cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)
    
    # Dibujar trayectoria
    #recorre la lista trayectoria desde el segundo punto (i = 1) hasta el último
    for i in range(1, len(trayectoria)):
        #cv2.line(imagen, punto anterior, punto actual, color, grosor)
        cv2.line(frame, trayectoria[i-1], trayectoria[i], (255, 255, 255), 2)

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.realease()
cv2.destroyAllWindows()
