# This is a sample Python script.
import os
import pytesseract
from PIL import Image, UnidentifiedImageError
from datetime import datetime

input_folder = 'images/'
output_folder = 'output/'


# Tutorial: https://www.educative.io/answers/how-to-extract-text-from-an-image-in-python
# Follow https://github.com/UB-Mannheim/tesseract/wiki#tesseract-installer-for-windows
# to install tesseract in your environment
# Add [images] you need to get text from into folder "images"
# All output file are in "output"
def print_image_to_text(file_path):
    # Define your tesseract_cmd
    tesseract_cmd = 'D:\\Programs\\tesser\\tesseract.exe'
    pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
    # Open the image file
    try:
        image = Image.open(file_path)
    except UnidentifiedImageError:
        print(file_path + " is not image file")
        return

    file_name = os.path.basename(file_path).split('.')[0]

    # Perform OCR using PyTesseract
    text = pytesseract.image_to_string(image)

    # Create output file
    now = datetime.now()
    output_file_name = output_folder + file_name + '-' + now.strftime("%m%d%Y%H%M%S") + '.txt'
    try:
        output_file = open(output_file_name, "w")
        output_file.write(text)
    except FileNotFoundError:
        print("Directory not exists")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Remove old file in output
    out_put_files = os.listdir(output_folder)
    for file in out_put_files:
        if os.path.exists(output_folder + file):
            os.remove(output_folder + file)

    files = os.listdir(input_folder)
    for file in files:
        print_image_to_text(input_folder + file)
