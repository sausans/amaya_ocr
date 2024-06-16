import pytesseract
from flask import Flask, request, jsonify
import os
from PIL import Image
import io

# Set the TESSDATA_PREFIX environment variable
os.environ["TESSDATA_PREFIX"] = "/app/tessdata"

app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def ocr():
    if 'image' not in request.files:
        return "No image uploaded", 400
    file = request.files['image']
    if file.filename == '':
        return "No selected file", 400
    image = Image.open(file.stream)
    extracted_text = pytesseract.image_to_string(image, lang='eng')
    return jsonify({"extracted_text": extracted_text})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
