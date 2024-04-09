import numpy as np
import cv2

image_data = np.array(
    [[0,0],
    [255,255]]
, dtype=np.uint8)

cv2.imwrite("0.png", image_data)

image_data = np.array(
    [[255, 255],
    [0, 0]]
, dtype=np.uint8)
cv2.imwrite("1.png", image_data)