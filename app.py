from flask import Flask, request, jsonify
import pytesseract
from PIL import Image
import io

app = Flask(__name__)

# Hardcode TESSDATA_PREFIX to the tessdata directory in the project
os.environ["TESSDATA_PREFIX"] = "/app/tessdata"

# Check if the path exists
if os.path.exists("/app/tessdata"):
    print("TESSDATA_PREFIX is set to: /app/tessdata")
else:
    print("Directory does not exist: /app/tessdata")

@app.route('/ocr', methods=['POST'])
def ocr():
    file = request.files['image']
    image = Image.open(io.BytesIO(file.read()))
    try:
        extracted_text = pytesseract.image_to_string(image, lang='eng')
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    return jsonify({"extracted_text": extracted_text})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
