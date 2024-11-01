import cv2

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    height, width, _ = frame.shape
    square_side = 100
    frame[height-square_side:, width-square_side:] = [0, 0, 0]
    frame[0:square_side, 0:square_side] = [0, 0, 0]
    frame[height - square_side:, 0:square_side] = [0, 0, 0]
    frame[0:square_side, width - square_side:] = [0, 0, 0]
    frame[((height-square_side) // 2):((height+square_side) // 2), ((width-square_side) // 2):((width+square_side) // 2)] = [0, 0, 0]
    cv2.imshow('camera', frame)
    key = cv2.waitKey(1)
    if key == ord(' '):
        break

cv2.destroyAllWindows()
cap.release()