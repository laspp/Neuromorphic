" Analyzation of the output neurons"
from collections import Counter

from tqdm import tqdm
from train import *


def accuracy(winners):
    """
    :param winners: list of dictionaries that contains pairs image-neuron.
    :return: accuracy - by defined criteria in the code
    """
    accuracy = 0
    for item in winners:
        value_counts = Counter(item.values())
        # dodati 1 kad nema duplikata
        multiple_occurrences = any(count > 1 for count in value_counts.values())
        # if True it means that there is a neuron that won for several images,
        # which means it didn't learn well
        # if false it means that iteration was correct.
        if not multiple_occurrences:
            accuracy += 1
    accuracy = (accuracy / len(winners)) * 100.0
    return accuracy



