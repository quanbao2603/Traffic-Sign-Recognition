import cv2
import numpy as np
from app.models.model_loader import model

async def predict_image(file):

    # đọc dữ liệu ảnh FE gửi lên
    img_bytes = await file.read()
    img_arr = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)

    if img is None:
        return {"error": "Không đọc được ảnh"}

    # chạy model YOLO đã train
    results = model(img)
    boxes = results[0].boxes

    if len(boxes) == 0:
        return {
            "label": "Không phát hiện biển báo",
            "confidence": 0.0,
            "bbox": None
        }

    # lấy box đầu tiên
    box = boxes[0]
    cls = int(box.cls)
    label = model.names[cls]
    conf = float(box.conf)
    bbox = box.xyxy.tolist()

    return {
        "label": label,
        "confidence": conf,
        "bbox": bbox
    }
