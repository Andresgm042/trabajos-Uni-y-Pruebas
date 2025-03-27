import cv2
import numpy as np

cap = cv2.VideoCapture(0)
gpu_canny = cv2.cuda.createCannyEdgeDetector(100,200)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.GaussianBlur(frame_gray, (5,5), 0)
    gpu_img = cv2.cuda_GpuMat()
    gpu_img.upload(frame_gray)

    gpu_bordes = gpu_canny.detect(gpu_img)
    bordes = gpu_bordes.download()
#contornos guarda contornos de imagen. _ solo es una variable que no se usa
    contornos, _ = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for conteo in contornos:
        area = cv2.contourArea(conteo)
        if area > 600:
        #aproxima el contorno a un poligono. True es para cerrar la figura
            perimetro = cv2.arcLength(conteo, True) 
        #0.02 es la precision del contorno. True es para cerrar la figura
            aprox = cv2.approxPolyDP(conteo, 0.02*perimetro, True)

            cv2.drawContours(frame, [aprox], -1, (0,255,0), 2)

            lados = len(aprox) #numero de lados del poligono
            x,y,w,h = cv2.boundingRect(aprox) #coordenadas
            if lados == 3:
                forma = "Tringulo"
            elif lados == 4:
                aspect_ratio = float(w)/h
                if aspect_ratio == 1:
                    forma = "Cuadrado"
                else:
                    forma = "Rectangulo"
            elif lados > 5:
                forma = "Circulo"
            else:
                forma = "Indefinido"
            #dibuja texto en la imagen
#cv2.putText(frame, texto, (x,y), fuente, tamano, color, grosor)
            cv2.putText(frame,forma,(x,y -10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)
    cv2.imshow('Reconocimiento de formas', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
