from ultralytics import YOLO

# Загружаем предобученную модель YOLOv8
model = YOLO('yolov8n.pt') # Выберите размер модели: n, s, m, l, x
# Запускаем обучение
model.train(data='config.yaml', epochs=10, batch=16, imgsz=640)
results = model.predict(source="C:/Users/user/Downloads/roki 2 photodata/WIN_20241030_10_58_23_Pro.jpg", conf=0.5)
results.show()