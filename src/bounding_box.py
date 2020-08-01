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
    # Read the image
    image = cv2.imread(file)

    # Add an subplot witb 1 row and 2 columns for original image and an image with bounding boxes
    fig = plt.figure(figsize=(13, 13))
    rows = 1
    columns = 2
    ax = []
    ax.append(fig.add_subplot(rows, columns, 1))
    ax[-1].set_title('Original Without Bounding Boxes')
    plt.imshow(image)

    # Now to plot box around a word rather then box around each character use pytesseract.image_to_data() function

    K = pytesseract.image_to_data(image, output_type=Output.DICT)
    print('Each word will be judged  on the Following Keys \n', K.keys())

    num_boxes = len(K['text'])
    for i in range(num_boxes):
        # TO only pick boxes with confidence  > 60%
        (x, y, w, h) = (K['left'][i], K['top']
                        [i], K['width'][i], K['height'][i])
        image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    b, g, r = cv2.split(image)
    img = cv2.merge([r, g, b])
    ax.append(fig.add_subplot(rows, columns, 2))
    ax[-1].set_title('Original With Bounding Boxes')
    plt.imshow(img)
    plt.show()


if __name__ == '__main__':
    main('images/sample1.jpg')
