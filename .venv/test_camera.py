import cv2
from ultralytics import YOLO

# Load mô hình đã huấn luyện
model = YOLO("runs/detect/train4/weights/best.pt")  # Đường dẫn đến mô hình của bạn

# Mở camera
cap = cv2.VideoCapture(0)  # 0 là camera mặc định, có thể đổi nếu cần

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Dự đoán với YOLO
    results = model(frame)

    # Vẽ bounding box lên ảnh
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Lấy tọa độ hộp
            conf = box.conf[0].item()  # Độ tin cậy
            cls = int(box.cls[0].item())  # Lớp nhận diện

            # Vẽ hình chữ nhật
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            label = f"{model.names[cls]} ({conf:.2f})"
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Hiển thị ảnh
    cv2.imshow("YOLO Traffic Sign Detection", frame)

    # Nhấn 'q' để thoát
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
