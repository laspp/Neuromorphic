import sys
from pathlib import Path
from train import train_net

def main(data_path=None, *other):
    if other:
        print(("Wrong number of arguments! {} given.\n"
               "Run:  python train.py [path to train data]\n").format(len(other)))
        exit()
    # Use default data set if no data given
    if not data_path:
        base_path = Path(__file__).parent.parent
        print(base_path)
        data_path = Path(base_path, 'data', 'MNIST_0-5')
    # data_path = Path(base_path, 'data', 'TOY_BINARY')
    # data_path = Path(base_path, 'data', 'BINARY_14')
    # data_path = Path(base_path, 'data', 'MNIST_TRAIN')

    print("Using training data in folder: ", data_path)
    train_net(data_path)

    # ovde pozvati klasifikacija


# Using the special variable
# __name__
if __name__ == "__main__":
    main(*sys.argv[1:])
