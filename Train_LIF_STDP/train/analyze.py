" Analyzation of the output neurons"
from collections import Counter


def analyze(winners):
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
    accuracy = (accuracy/len(winners))*100.0
    return accuracy

# dict = {'0': 0, '1': 1, '2': 2, '3': 3}
# dict2 = {'0': 0, '1': 2, '2': 42, '3': 44}
# dict3 = {'0': 0, '1': 1, '2': 3, '3': 35}
# lista = []
# lista.append(dict)
# lista.append(dict2)
# lista.append(dict3)
#
# a = analyze(lista)
# print(a)