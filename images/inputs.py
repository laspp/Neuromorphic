import numpy as np
from PIL import Image

image_data = np.array([
    [[0, 0, 0], [0, 0, 0]],
    [[255, 255, 255], [255, 255, 255]]
], dtype=np.uint8)

image = Image.fromarray(image_data)
image.save("0.png")

image_data = np.array([
    [[255, 255, 255], [255, 255, 255]],
    [[0, 0, 0], [0, 0, 0]]
], dtype=np.uint8)
image = Image.fromarray(image_data)
image.save("1.png")