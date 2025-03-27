import cv2
import numpy as np

cap = cv2.VideoCapture(0)
gpu_canny = cv2.cuda.createCannyEdgeDetector(100,200)

while True:
    ret,frame = cap.read()
    if not ret:
        break

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #filtro gaussiano(5x5 reduce ruido, 0 es la desviacion)
    #en 0 opencv calcula la desviacion
    frame_gray = cv2.GaussianBlur(frame_gray, (5,5), 0) 

    gpu_img = cv2.cuda_GpuMat()
    gpu_img.upload(frame_gray)

    gpu_edges = gpu_canny.detect(gpu_img)
    bordes = gpu_edges.download()

    cv2.imshow("Filtro gaussiano", bordes)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
