from flask import Flask, request, jsonify
import cv2
import numpy as np
from ultralytics import YOLO

app = Flask(__name__)

model = YOLO("yolov8m.pt")
#TARGET_CLASSES = [0, 2]  # Customize target classes

@app.route('/get_detection', methods=['POST'])
def get_detection():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    file = request.files['image']
    npimg = np.frombuffer(file.read(), np.uint8)
    frame = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    # Perform YOLO detection
    results = model(frame)
    detections = []
    for result in results:
        for cls, bbox in zip(result.boxes.cls.cpu(), result.boxes.xyxy.cpu()):
            #if int(cls) in TARGET_CLASSES:
                detections.append({
                    "class": int(cls),
                    "bbox": bbox.tolist()
                })

    return jsonify(detections)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
