import requests

# Define the Heroku app URL
OCR_URL = "https://amayaocr-ad272d951465.herokuapp.com/ocr"

def process_image(image_path):
    try:
        # Open the image file in binary mode
        with open(image_path, "rb") as image_file:
            # Send the image to the OCR endpoint
            response = requests.post(OCR_URL, files={"image": image_file})
            response.raise_for_status()
            # Get the OCR result from the response
            extracted_text = response.json().get("text", "")
            return extracted_text
    except Exception as e:
        print(f"Error processing image: {e}")
        return ""

if __name__ == "__main__":
    # Path to the local image file
    image_path = "screenshot.png"  # Replace with your actual image file path
    extracted_text = process_image(image_path)
    print(f"Extracted Text: {extracted_text}")
