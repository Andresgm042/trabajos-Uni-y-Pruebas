#MOG2 es un sustractor de fondo
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

#se crea sustractor de fondo
fondo_sustrac = cv2.cuda.createBackgroundSubtractorMOG2()

#----------------------------------------------------------------
def conseguir_frame():
    ret, frame0 = cap.read()
    if not ret or frame0 is None:
        print("No se pudo conseguir el frame")
        return None
    return frame0
    
def up_gpu(frame0):
    gpu_frame0 = cv2.cuda_GpuMat()
    gpu_frame0.upload(frame0)
    return gpu_frame0


while True:
    frame = conseguir_frame()
    gpu_frame = up_gpu(frame)

    stream = cv2.cuda.Stream()

    #aplicar MOG2 en frame
    gpu_bgmask = fondo_sustrac.apply(gpu_frame, learningRate = -1, stream = stream)

    #lo bajamos a la cpu
    bgmask = gpu_bgmask.download()

    contornos, _ = cv2.findContours(bgmask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour in contornos:
        if cv2.contourArea(contour) > 800:
            x, y, w, h = cv2.boundingRect(contour)
            #donde dibujarlo, coords, no se, color, grosor
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    cv2.imshow("Frame", frame)
    #cv2.imshow("Foreground Mask", bgmask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
