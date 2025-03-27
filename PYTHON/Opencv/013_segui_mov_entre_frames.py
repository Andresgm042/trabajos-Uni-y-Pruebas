import cv2
import numpy as np

cap = cv2.VideoCapture(0)

#empiezo a hacer funciones porque ya se esta volviendo bien desorganizado

def escala_grises(frame):
    #se pasa a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #filtro gaussiano para reducir ruido 21x21
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    return gray

def calc_diferencia(frame1, frame2):
    frame_dif = cv2.absdiff(frame1, frame2)
    return frame_dif
#------------------------------------------------------------------------------

ret, frame1 = cap.read()
if not ret:
    print("No hay camara")
    cap.release()
    exit()

gray1 = escala_grises(frame1)

while True:

    ret, frame2 = cap.read()
    if not ret:
        print("No hay camara")
        break

    gray2 = escala_grises(frame2)

    frame_diff = calc_diferencia(gray1, gray2)

    #umbral para detectar regiones en movimiento 
    #threshold convierte el frame a blanco y negro
    #pixeles con diferencia menor a 25 se ponen en negro (sin mov) (25)
    #pixeles con diferencia mayor a 25 se ponen en blanco (255)
    _, thresh = cv2.threshold(frame_diff, 25, 255, cv2.THRESH_BINARY)

    #encontrar contornos de las areas en movimiento
    contours, _ =cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) > 800:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame2, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Frame", frame2)
    #actualiza el frame anterior
    gray1 = gray2.copy()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllwindows()