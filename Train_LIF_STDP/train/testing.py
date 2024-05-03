# TODO: napraviti testing, da pozove npr svaki data set, i analizira
# na kraju ispise
import os
import sys
from pathlib import Path
from pprint import pprint

import cv2
import winsound
from matplotlib import pyplot as plt
from tqdm import tqdm
from train import train_net
from accuracy import accuracy

base_path = Path(__file__).parent.parent
print(base_path)
data_path = Path(base_path, 'data', 'MNIST_0-5')
#data_path = Path(base_path, 'data', 'TOY_BINARY')
#data_path = Path(base_path, 'data', 'BINARY_14')
#data_path = Path(base_path, 'data', 'MNIST_TRAIN')

print("Using training data in folder: ", data_path)
image_file = next(data_path.glob('*.png'), None)
img = cv2.imread(str(image_file))
pixel_x, _, _ = img.shape

last_winners = []
# Redirect standard output to a null device (suppression)
original_stdout = sys.stdout
sys.stdout = open(os.devnull, 'w')


for i in tqdm(range(1), colour='GREEN'):
    _, last = train_net(data_path, pixel_x, display_plots=False)
    last_winners.append(last)
sys.stdout = original_stdout
pprint(last_winners)
accuracy = accuracy(last_winners, data_path)
print(str(accuracy) + " %")
winsound.MessageBeep()


