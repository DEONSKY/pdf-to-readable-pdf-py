from PIL import Image

import pytesseract

from skimage.filters import threshold_otsu
import skimage.io
import skimage.color
import skimage.filters
import matplotlib.pyplot as plt

# If you don't have tesseract executable in your PATH, include the following:
#pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

'''
# Simple image to string
print(pytesseract.image_to_string(Image.open('test.jpg')))

# In order to bypass the image conversions of pytesseract, just use relative or absolute image path
# NOTE: In this case you should provide tesseract supported images or tesseract will return error
print(pytesseract.image_to_string('test.jpg'))
# List of available languages
print(pytesseract.get_languages(config=''))

# French text image to string
print(pytesseract.image_to_string(Image.open('test.jpg'), lang='tur'))

# Batch processing with a single file containing the list of multiple image file paths
#print(pytesseract.image_to_string('images.txt'))

# Timeout/terminate the tesseract job after a period of time
try:
    print(pytesseract.image_to_string('test.jpg', timeout=2)) # Timeout after 2 seconds
    print(pytesseract.image_to_string('test.jpg', timeout=0.5)) # Timeout after half a second
except RuntimeError as timeout_error:
    # Tesseract processing is terminated
    pass

# Get bounding box estimates
print(pytesseract.image_to_boxes(Image.open('test.jpg')))

# Get verbose data including boxes, confidences, line and page numbers
print(pytesseract.image_to_data(Image.open('test.jpg')))

# Get information about orientation and script detection
print(pytesseract.image_to_osd(Image.open('test.jpg')))
'''
image = skimage.io.imread('test3.jpg')
gray_image = skimage.color.rgb2gray(image)
#blurred_image = skimage.filters.gaussian(gray_image, sigma=1.0)
tresh = threshold_otsu(gray_image)
sharp = skimage.filters.unsharp_mask(gray_image, radius=20, amount=1)
skimage.io.imsave('foo.jpg',sharp)

post_processed_image =  'foo.jpg'
print("1")
# Get a searchable PDF
pdf = pytesseract.image_to_pdf_or_hocr(post_processed_image, lang='tur', extension='pdf',config="--psm 1 -c tessedit_char_blacklist=|[]©>/")
with open('test.pdf', 'w+b') as f:
    f.write(pdf) # pdf type is bytes by default
print("2")
# Get HOCR output
hocr = pytesseract.image_to_pdf_or_hocr(post_processed_image, lang='tur',config="-c tessedit_char_blacklist=|[]©>/")
print("3")
print(pytesseract.image_to_string(post_processed_image, lang='tur',config="-c tessedit_char_blacklist=|[]©>/"))
# Get ALTO XML output
print("4")