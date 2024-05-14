from pprint import pprint

import numpy as np
import seaborn
from matplotlib import pyplot as plt, animation


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

def animate_learning(total_syns):
    fig = plt.figure(figsize=(8, 6))
    total_syns *= 100
    pprint(total_syns)
    struktura = total_syns[:, ::2, 2, :]
    print("Sve epohe, samo nulta slika, samo drugi neuron, sve sinapse")
    pprint(struktura)
    print(np.shape(struktura))
    jedna_epoha = struktura[0, :, :]
    pprint(jedna_epoha)
    sinapse = jedna_epoha.reshape((2, 2))
    print(np.shape(sinapse))
    pprint(sinapse)
    ani = animation.FuncAnimation(fig, update, frames=20, interval=300, fargs=[total_syns])
    plt.show()
    #ani.save('anim.gif', writer='imagemagick', fps=60)



def update(frame, total_syns):
    plt.clf()
    num_neurons = total_syns.shape[2]
    for i in range(num_neurons):
        plt.clf()
        heatmap = plt.imshow(total_syns[frame, ::2, i, :].reshape((2, 2)), cmap='hot', interpolation='nearest')
        plt.title('Epoch: {}'.format(frame + 1))
        plt.colorbar(heatmap)
    # od te strukture uzeti tu epohu koja je num

