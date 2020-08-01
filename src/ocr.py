import re
import cv2
import numpy as np
import pytesseract
from pytesseract import Output
import matplotlib.pyplot as plt

try:
    import src.preprocessing as preprocessing
except:
    import preprocessing


def main(file):
    # preprocessing the image
    image = cv2.imread(file)
    gray = preprocessing.get_grayscale(image)

    # Plot images after preprocessing

    # plt.imshow(gray)
    # plt.show()

    custom_config = r'--oem 3 --psm 6'
    # produce the output of Tesseract
    print(pytesseract.image_to_string(image, config=custom_config))


if __name__ == '__main__':
    main('images/Lorem.jpg')
