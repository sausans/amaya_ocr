import os

tessdata_dir = "/usr/share/tesseract-ocr/4.00/tessdata/"

if os.path.exists(tessdata_dir):
    print(f"Directory exists: {tessdata_dir}")
    print("Contents:")
    for filename in os.listdir(tessdata_dir):
        print(filename)
else:
    print(f"Directory does not exist: {tessdata_dir}")
