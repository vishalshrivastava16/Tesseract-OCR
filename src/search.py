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


def main(file, regEx):
    image = cv2.imread(file)
    # Replace the regex expression if you want to search for particular text
    K = pytesseract.image_to_data(image, output_type=Output.DICT)

    num_boxes = len(K['text'])

    for i in range(num_boxes):
        if int(K['conf'][i]) > 60:
            if re.match(regEx, K['text'][i]):
                (x, y, w, h) = (K['left'][i], K['top']
                                [i], K['width'][i], K['height'][i])
                image = cv2.rectangle(
                    image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    b, g, r = cv2.split(image)
    rgb_img = cv2.merge([r, g, b])
    plt.figure(figsize=(16, 12))
    plt.imshow(rgb_img)
    plt.title('SAMPLE WITH BOXES FOR DATES')
    plt.show()


if __name__ == '__main__':
    main('images/sample3.jpg', "^([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])(\.|-|/)([1-9]|0[1-9]|1[0-2])(\.|-|/)([0-9][0-9]|19[0-9][0-9]|20[0-9][0-9])$|^([0-9][0-9]|19[0-9][0-9]|20[0-9][0-9])(\.|-|/)([1-9]|0[1-9]|1[0-2])(\.|-|/)([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])$")
