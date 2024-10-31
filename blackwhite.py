import cv2

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    height, width, _ = frame.shape
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('camera', grayscale)
    key = cv2.waitKey(1)
    if key == ord(' '):
        break

cv2.destroyAllWindows()
cap.release()