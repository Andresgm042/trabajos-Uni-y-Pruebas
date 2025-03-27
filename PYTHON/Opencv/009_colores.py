import cv2
import numpy as np

cap = cv2.VideoCapture(0)
gpu_canny = cv2.cuda.createCannyEdgeDetector(100,200)

while True:
    ret,frame = cap.read()
    if not ret:
        break
    
    #convertir frame de BGR a HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Formato HSV (tipo de color, saturacio, brillo)
    lower_red = np.array([0, 120, 70]) #limite inferior del rango de rojo
    upper_red = np.array([10, 255, 255]) #limite superior del rango de rojo

    mask = cv2.inRange(hsv, lower_red, upper_red)

    #aplicar la mascara al frame original
    #bitwise_and: aplica una operacion AND a los pixeles de dos imagenes
    #
    resultado = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Filtro de color", resultado)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()