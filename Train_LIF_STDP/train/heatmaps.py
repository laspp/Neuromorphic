import seaborn
from matplotlib import pyplot as plt


def plotting_potentials(display_plots, ttt, Pth, pot_arrays):
    fig, axs = plt.subplots(3, 3)
    # TODO PAMETNIJE
    k = 0
    for i in range(3):
        for j in range(3):
            axs[i, j].set_title(f"Neuron {k}")
            axs[i, j].plot(ttt, Pth, 'r')
            axs[i, j].plot(ttt, pot_arrays[k])
            k += 1
    if display_plots:
        plt.tight_layout()
        plt.show()

def synapse_heatmap(synapse, display_plots):
    for i, per_neuron in enumerate(synapse):
        reshape = per_neuron.reshape((2, 2))
        seaborn.heatmap(reshape)
        if display_plots:
            plt.title(f"Neuron {i}")
            plt.show()