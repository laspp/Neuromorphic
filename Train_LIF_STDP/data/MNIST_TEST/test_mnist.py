import os
import tensorflow as tf
from PIL import Image

# Load MNIST dataset
mnist = tf.keras.datasets.mnist

# Load only digits 0 to 5
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

test_mask = (test_labels <= 5)
test_images, test_labels = test_images[test_mask], test_labels[test_mask]



# Get the current working directory
current_dir = os.getcwd()


for i, image in enumerate(test_images):
    image_path = os.path.join(current_dir, f"test_image_{i}.png")
    Image.fromarray(image).save(image_path)

print("Images saved successfully.")

