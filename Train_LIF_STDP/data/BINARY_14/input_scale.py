from pprint import pprint

import numpy as np
import cv2

matrix = np.zeros((14, 14))
matrix[7:, :] = 255
#pprint(matrix)
print(np.sum(matrix))

image_data = np.array(
    matrix
, dtype=np.uint8)

cv2.imwrite("0.png", image_data)

matrix = np.zeros((14, 14))
#matrix[:, :] = 255
matrix[:7, :] = 255

image_data = np.array(
    matrix
, dtype=np.uint8)
cv2.imwrite("1.png", image_data)