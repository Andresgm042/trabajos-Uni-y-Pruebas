import cv2

cap = cv2.VideoCapture(0) #abra la camara

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)  # Detección de bordes

    cv2.imshow("Original", frame)
    cv2.imshow("Bordes", edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
