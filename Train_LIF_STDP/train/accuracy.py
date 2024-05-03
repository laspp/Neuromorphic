" Analyzation of the output neurons"
from collections import Counter

import cv2
from tqdm import tqdm
from train import *
import numpy as np


def accuracy(winners, data_path):
    """
    :param winners: list of dictionaries that contains pairs image-neuron.
    :return: accuracy - by defined criteria in the code
    """
    base_path = Path(__file__).parent.parent
    reconstructs_path = Path(base_path, 'reconstructs')
    print(reconstructs_path)
    accurate = 0
    len = 0
    for dict in winners:
        # item je recnik s parovima input-output
        for k, v in dict.items():
            # k je input, v je output
            print(k)            # 0.png
            print(v)            # 0
            input_path = os.path.join(data_path, k)
            input = cv2.imread(input_path, 0)
            vv = f"neuron{v}.png"
            output_path = os.path.join(reconstructs_path, vv)
            output = cv2.imread(output_path, 0)
            mse = compute_mse(input, output)
            print(f"Mse je {mse}")
            len += 1

            if data_path == Path(base_path, 'data', 'MNIST_0-5'):
                if mse < 20:
                    accurate +=1
            elif data_path == Path(base_path, 'data', 'TOY_BINARY'):
                if mse < 0.25:
                    accurate +=1
            elif data_path == Path(base_path, 'data', 'BINARY_14'):
                if mse < 0.25:
                    accurate += 1
            else:
                raise Exception("Invalid data path for testing")
# za MNIST: ispod 14 su okej, 52 je samo sum
# za TOY
# za BINARY 14
    return (accurate/len)*100.0


def compute_mse(input, output):
    assert input.shape == output.shape
    squared_diff = (input - output) ** 2
    mse = np.mean(squared_diff)
    return mse
