import cv2

# Intenta abrir la cámara en /dev/video0
cap = cv2.VideoCapture(0) #Abre la cámara 0 indica la cámara predeterminada)

if not cap.isOpened(): #si la cámara se abrió correctamente
    print("No se pudo abrir la cámara")
else:
    print("Cámara detectada, mostrando imagen...")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("No se pudo obtener el frame")
            break

        cv2.imshow("Cámara Jetson", frame)

        # Presiona 'q' para salir
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
