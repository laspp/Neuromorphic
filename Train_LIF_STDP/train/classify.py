# ovde klasifikacija
import sys
from pathlib import Path
import numpy as np

from train import train_net
from neuron import neuron

# ovde uzme sinapse i pusti podatke i vrati rezyultat, moye i tacnost da vrati
# Defining main function
def main(data_path=None, *other):
    if other:
        print(("Wrong number of arguments! {} given.\n"
               "Run:  python train.py [path to train data]\n").format(len(other)))
        exit()
    # Use default data set if no data given
    if not data_path:
        base_path = Path(__file__).parent.parent
        print(base_path)
        data_path = Path(base_path, 'data', 'MNIST_TRAIN')

    print("Using training data in folder: ", data_path)
    synapse = train_net(data_path)


# Using the special variable
# __name__
if __name__ == "__main__":
    main(*sys.argv[1:])