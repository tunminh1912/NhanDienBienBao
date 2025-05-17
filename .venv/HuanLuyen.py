from ultralytics import YOLO

# Load model YOLOv8 có sẵn
model = YOLO("yolov8n.pt")  # Có thể thay bằng yolov8s.pt, yolov8m.pt nếu muốn mô hình mạnh hơn

# Huấn luyện mô hình
model.train(data="data.yaml", epochs=50, imgsz=640, batch=16, device='cpu')

