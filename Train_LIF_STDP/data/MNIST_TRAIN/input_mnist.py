import os
import numpy as np
import tensorflow as tf
from PIL import Image

# Load MNIST dataset
mnist = tf.keras.datasets.mnist

# Load only digits 0 to 5
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
train_mask = (train_labels <= 5)
train_images, train_labels = train_images[train_mask], train_labels[train_mask]

# Get indices of images for each digit from 0 to 5
digit_indices = {digit: [] for digit in range(6)}
for i, label in enumerate(train_labels):
    if len(digit_indices[label]) < 5:
        digit_indices[label].append(i)
    if all(len(indices) >= 5 for indices in digit_indices.values()):
        break

# Select 20 images for each digit from 0 to 5
selected_images = []
selected_labels = []
for digit, indices in digit_indices.items():
    selected_images.extend(train_images[indices])
    selected_labels.extend(train_labels[indices])

selected_images = np.array(selected_images)
selected_labels = np.array(selected_labels)


# Get the current working directory
current_dir = os.getcwd()

# Save the images
for i, image in enumerate(selected_images):
    image_path = os.path.join(current_dir, f"train_image_{i}.png")
    Image.fromarray(image).save(image_path)


print("Images saved successfully.")

# 13.14 pocelo