" Analyzation of the output neurons"
from collections import Counter

import cv2
from tqdm import tqdm
from train import *
import numpy as np


def accuracy_mse(winners, data_path):
    """
    :param winners: list of dictionaries that contains pairs image-neuron.
    :return: accuracy - by defined criteria in the code
    """
    base_path = Path(__file__).parent.parent
    reconstructs_path = Path(base_path, 'reconstructs')
    accuracy = 0
    for dict in winners:
        # dict je recnik s parovima input-output
        acc_flag = True
        print(f"-------{dict}-------")
        for k, v in dict.items():
            # k je input, v je output
            print(f"{k} : {v}")
            input_path = os.path.join(data_path, k)
            input = cv2.imread(input_path, 0)
            vv = f"neuron{v}.png"
            output_path = os.path.join(reconstructs_path, vv)
            output = cv2.imread(output_path, 0)
            mse = compute_mse(input, output)
            print(f"Mse je {mse}")
            mae = compute_mae(input, output)
            print(f"Mae je {mae}")


            if data_path == Path(base_path, 'data', 'MNIST_0-5'):
                if mse < 20:
                    # ok: 12.4, 5.3, 11.5, 13.6
                    # ne: 54.3, 56, 62
                    acc_flag = True
                else:
                    acc_flag = False
                    break
            elif data_path == Path(base_path, 'data', 'TOY_BINARY'):
                # 33.25 ne, 16 moze da prodje ali zavisi slucaj, nekad bas ne
                # nekad i 30.25 moze, treba mozda promeniti kriterijum
                # <42.25, 71.25 ne valja, 58.25 ne, 0.5 daje skroz belu
                # 4.25 nije ok
                # inicijalno <26
                if mse < 26:        # jer je mali problem
                    acc_flag = True
                else:
                    acc_flag = False
                    break
            elif data_path == Path(base_path, 'data', 'BINARY_14'):
                if mse < 31:
                    # ispod 42 sigurno, nekad ni 16.25 nije skroz dobro, 12.25 ok nekad, nekad uopste ne
                    acc_flag = True
                else:
                    acc_flag = False
                    break
            else:
                raise Exception("Invalid data path for testing")

        # na kraju recnika, ako je sve bilo tacno:
        value_counts = Counter(dict.values())
        multiple_occurrences = any(count > 1 for count in value_counts.values())
        # if True it means that there is a neuron that won for several images,
        # which means it didn't learn well
        if acc_flag and not multiple_occurrences:
            accuracy += 1

    accuracy = (accuracy / len(winners)) * 100
    # TODO: upisati u fajl
    return accuracy


def accuracy_mae(winners, data_path):
    """
    :param winners: list of dictionaries that contains pairs image-neuron.
    :return: accuracy - by defined criteria in the code
    """
    base_path = Path(__file__).parent.parent
    reconstructs_path = Path(base_path, 'reconstructs')
    accuracy = 0
    for dict in winners:
        # item je recnik s parovima input-output
        acc_flag = True
        #print(f"-------{dict}-------")
        for k, v in dict.items():
            # k je input, v je output
            #print(f"{k} : {v}")
            input_path = os.path.join(data_path, k)
            input = cv2.imread(input_path, 0)
            vv = f"neuron{v}.png"
            output_path = os.path.join(reconstructs_path, vv)
            output = cv2.imread(output_path, 0)
            mae = compute_mae(input, output)
            #print(f"Mae je {mae}")

            if data_path == Path(base_path, 'data', 'MNIST_0-5'):
                # ok: 21.53, 13.5, 16.8, 22.8, 25.8, 27.1
                # ne: 37.3, 36, 32.7
                if mae < 28:
                    acc_flag = True
                else:
                    acc_flag = False
                    break
            elif data_path == Path(base_path, 'data', 'TOY_BINARY'):
                # 11.25 ne valja, 5.25 ne valja, 14.25 ne, 0.5 daje skroz belu
                # inicijalno < 5.25
                if mae < 5.25:
                    acc_flag = True
                else:
                    acc_flag = False
                    break
            elif data_path == Path(base_path, 'data', 'BINARY_14'):
                if mae < 9:
                    # ispod 42 sigurno, nekad ni 16.25 nije skroz dobro, 12.25 ok nekad, nekad uopste ne
                    acc_flag = True
                else:
                    acc_flag = False
                    break
            else:
                raise Exception("Invalid data path for testing")
        # za MNIST: ispod 14 su okej, 52 je samo sum
        # za TOY
        # za BINARY 14
        # na kraju recnika, ako je sve bilo tacno:
        value_counts = Counter(dict.values())
        multiple_occurrences = any(count > 1 for count in value_counts.values())
        # if True it means that there is a neuron that won for several images,
        # which means it didn't learn well
        if acc_flag and not multiple_occurrences:
            accuracy += 1
    accuracy = (accuracy/len(winners))*100
    return accuracy

def compute_mse(input, output):
    assert input.shape == output.shape
    squared_diff = (input - output) ** 2
    mse = np.mean(squared_diff)
    return mse

def compute_mae(input, output):
    assert input.shape == output.shape
    abs_diff = np.abs(input - output)
    mae = np.mean(abs_diff)
    return mae