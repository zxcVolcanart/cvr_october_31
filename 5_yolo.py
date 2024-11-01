from ultralytics import YOLO
import cv2
from ultralytics.utils.plotting import Annotator  # ultralytics.yolo.utils.plotting is deprecated

model = YOLO('best.pt')
cap = cv2.imread("C:/Users/user/Downloads/roki 2 photodata/WIN_20241030_10_56_25_Pro (2).jpg")

img = cap

    # BGR to RGB conversion is performed under the hood
    # see: https://github.com/ultralytics/ultralytics/issues/2575
results = model.predict(img)

for r in results:

    annotator = Annotator(img)

    boxes = r.boxes
    for box in boxes:
        b = box.xyxy[0]  # get box coordinates in (top, left, bottom, right) format
        c = box.cls
        annotator.box_label(b, model.names[int(c)])

    img = annotator.result()
    while True:
        cv2.imshow('YOhttps://habr.com/ru/articles/593547/LO V8 Detection', img)
        if cv2.waitKey(1) & 0xFF == ord(' '):
            break
