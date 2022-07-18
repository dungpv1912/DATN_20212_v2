import cv2

cap = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_PLAIN

while (True):

    success, frame = cap.read()
    if success != True:
        break
    image = frame.copy()

    cv2.imshow("Image", image)

    key = cv2.waitKey(1)
    if cv2.waitKey(25) & 0xFF == ord('q'):  # bấm phím Q để thoát
        break

cap.release()
cv2.destroyAllWindows()
