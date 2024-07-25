from flask import Flask, request, jsonify
import torch
import cv2
import numpy as np
import base64
from PIL import Image
from io import BytesIO

app = Flask(__name__)

# Modeli yükle
model = torch.hub.load("ultralytics/yolov5", "yolov5s")

def image_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

@app.route('/detect/<label>', methods=['POST'])
def detect(label):
    data = request.json
    image_data = data.get('image')  # Base64 encoded image
    if not image_data:
        return jsonify({'error': 'No image provided'}), 400

    # Convert Base64 to image
    image_bytes = base64.b64decode(image_data)
    image = Image.open(BytesIO(image_bytes))

    # Make a prediction
    results = model(image, size=640)

    # Convert the results to JSON format
    predictions = results.pandas().xyxy[0].to_dict(orient='records')

    # Filter by label
    if label:
        predictions = [p for p in predictions if p['name'] == label]
    
    # Return the results as JSON
    response = {
        'image': image_to_base64(image),
        'objects': predictions,
        'count': len(predictions),
    }

    return jsonify(response)

@app.route('/detect', methods=['POST'])
def detect_no_label():
    return detect(None)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)