import cv2
from pprint import pprint

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    print(ret)
    pprint(frame)
    cv2.imshow('camera', frame)
    cv2.waitKey(1)
    break
