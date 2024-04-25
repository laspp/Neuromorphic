from pprint import pprint

import numpy as np
import cv2

matrix = np.zeros((2, 2))
matrix[14:, :] = 255
matrix = [[0, 0], [255, 255]]
#pprint(matrix)
print(np.sum(matrix))

image_data = np.array(
    matrix
, dtype=np.uint8)

cv2.imwrite("0.png", image_data)

matrix = np.zeros((2, 2))
#matrix[:, :] = 255
matrix = [[255, 255], [0, 0]]

image_data = np.array(
    matrix
, dtype=np.uint8)
cv2.imwrite("1.png", image_data)


