from flask import Flask, request, jsonify
import pytesseract
from PIL import Image
import io

app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def ocr():
    file = request.files['image']
    image = Image.open(io.BytesIO(file.read()))
    text = pytesseract.image_to_string(image)
    return jsonify({'text': text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
