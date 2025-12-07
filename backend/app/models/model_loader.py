import os
from ultralytics import YOLO

# BASE_DIR = thư mục gốc dự án traffic-sign-recognition/
BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "..")
)

# Đường dẫn tới model/best.pt
MODEL_PATH = os.path.join(BASE_DIR, "model", "best.pt")

print("📌 Loading YOLO model from:", MODEL_PATH)

# Load model YOLO đã train
model = YOLO(MODEL_PATH)