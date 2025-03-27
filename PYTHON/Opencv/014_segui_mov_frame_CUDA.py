import cv2
import numpy as np

cap = cv2.VideoCapture(0)

#empiezo a hacer funciones porque ya se esta volviendo bien desorganizado

def frame():
    ret, frame0 = cap.read()
    if not ret or frame0 is None:
        print("No se pudo capturar el frame")
        return None
    return frame0

def escala_grises(frame):
    #se pasa a escala de grises
    gray = cv2.cuda.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #se crea filtro gaussiano, con cuda no se puede usar directamente
    filt_gauss = cv2.cuda.createGaussianFilter(
        srcType = gray.type(),
        dstType = gray.type(),
        ksize = (21,21),
        sigma1 = 0
    )
    #se aplica el filtro
    gray_gauss = filt_gauss.apply(gray)
    return gray_gauss

def calc_diferencia(frame1, frame2):
    frame_dif = cv2.cuda.absdiff(frame1, frame2)
    return frame_dif
#------------------------------------------------------------------------------

frame1 = frame()
gpu_frame1 = cv2.cuda_GpuMat()
gpu_frame1.upload(frame1)
gpu_gray1 = escala_grises(gpu_frame1)

while True:

    frame2 = frame()
    gpu_frame2 = cv2.cuda_GpuMat()
    gpu_frame2.upload(frame2)
    gpu_gray2 = escala_grises(gpu_frame2)

    gpu_diff = calc_diferencia(gpu_gray1, gpu_gray2)

    #umbral para detectar regiones en movimiento 
    _, gpu_thresh = cv2.cuda.threshold(gpu_diff, 25, 255, cv2.THRESH_BINARY)

    #bajamos el umbral de la gpu
    thresh = gpu_thresh.download()

    #encontrar contornos de las areas en movimiento
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) > 1000:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame2, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Frame", frame2)

    #actualiza el frame anterior, ahora con clone porque ahora esta en CUDA
    gpu_gray1 = gpu_gray2.clone()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllwindows()