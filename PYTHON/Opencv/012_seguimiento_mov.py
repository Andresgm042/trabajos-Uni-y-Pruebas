import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("No hay camara")
        break

    #coord x, y. ancho y altura (50x50)
    x, y, w, h = 200, 150, 50, 50

    #region de interes, la region donde sigue el objeto
    roi = frame[y:y+h, x:x+w]

    hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)#convertir a HSV
    #calcula histograma
    #0: usa el canal H (tono). 180:divide lo tonos en 180 rangos. 0, 180: rango del tono
    roi_hist = cv2.calcHist([hsv_roi], [0], None, [180], [0, 180])

    #Normalizar, ajusta los valores del histograma en rango 0 y 255
    cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

    #criterios de parada de camshift, maximo 10 iteraciones
    #si se mueve menos de un pixel, detener actualizacion
    #detener cuando se alcance precision o un numero maximo de intentos
    term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

    gpu_frame = cv2.cuda_GpuMat()
    gpu_frame.upload(frame)

    gpu_hsv = cv2.cuda.cvtColor(gpu_frame, cv2.COLOR_BGR2HSV)
    hsv = gpu_hsv.download()

    #compara histograma del objeto con el frame actual
    back_proj = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

    #frame con zonas donde el onjeto puede estar, posicion iniciañ del objeto,
    #conidicones para detenerse
    ret, track_window = cv2.CamShift(back_proj, (x, y, w, h), term_crit)

    pts = cv2.boxPoints(ret)
    pts = np.int0(pts)
    cv2.polylines(frame, [pts], True, (0, 255, 0), 2)

    x, y, w, h = track_window
    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllwindows()