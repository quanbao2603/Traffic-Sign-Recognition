import os
from ultralytics import YOLO

# Lấy đường dẫn tuyệt đối đến thư mục app
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Đường dẫn đến model
MODEL_PATH = os.path.join(BASE_DIR, "model", "best.pt")

print("🔍 Loading model from:", MODEL_PATH)

model = YOLO(MODEL_PATH)