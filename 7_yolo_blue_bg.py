from ultralytics import YOLO
import cv2
from ultralytics.utils.plotting import Annotator  # ultralytics.yolo.utils.plotting is deprecated

model = YOLO('yolov8n.pt')
cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()

    # BGR to RGB conversion is performed under the hood
    # see: https://github.com/ultralytics/ultralytics/issues/2575
    results = model.predict(img)

    for r in results:

        annotator = Annotator(img)

        boxes = r.boxes
        for box in boxes:
            b = box.xyxy[0]  # get box coordinates in (top, left, bottom, right) format
            c = box.cls
            if model.names[int(c)] == 'person':
                annotator.box_label(b, model.names[int(c)])
                top, left, bottom, right = b.numpy().astype(int)
                img[left:right, top:bottom, 0] = 255

    img = annotator.result()
    cv2.imshow('YOhttps://habr.com/ru/articles/593547/LO V8 Detection', img)
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break

cap.release()
cv2.destroyAllWindows()
