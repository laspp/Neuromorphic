import math
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
            axs[i, j].set_ylim((0 - Pth[0]*1.1), Pth[0]*1.1)
            axs[i, j].plot(ttt, pot_arrays[k])
            k += 1
    if display_plots:
        plt.tight_layout()
        plt.show()

def synapse_heatmap(synapse, display_plots):
    for i, per_neuron in enumerate(synapse):
        reshape = per_neuron.reshape((2, 2))
        seaborn.heatmap(reshape, cmap='Grays')
        if display_plots:
            plt.title(f"Neuron {i}")
            plt.show()

def animate_learning(total_syns):
    fig = plt.figure(figsize=(8, 6))
    print(np.shape(total_syns))
    print(total_syns.shape[0])
    print(total_syns[0, ::2, 0, :])
    ani = animation.FuncAnimation(fig, update_anim, frames=total_syns.shape[0]*total_syns.shape[2], interval=100, fargs=[total_syns], repeat=False)
    ani.repeat = False
    ani.save('anim.gif', writer='ffmpeg', fps=60)
    plt.show()


def update_anim(frame, total_syns):
    plt.clf()
    num_synapses = total_syns.shape[3]
    num_neurons = total_syns.shape[2]
    num_inputs = total_syns.shape[1]
    num_epochs = total_syns.shape[0]
    current_neuron = frame // num_epochs
    current_epoch = frame % num_epochs
    heatmap = plt.imshow(total_syns[current_epoch, ::2, current_neuron, :].reshape((2, 2)), cmap='Purples', interpolation='nearest')
    plt.title(f"Input: '0.png'\nEpoch: {current_epoch}, Neuron {current_neuron}")
    plt.colorbar(heatmap)

def plot_trains(train, title, synapse=[1, 1, 1, 1]):
    """
    	:param: train is a list (size pixel_x*pixel_x) that contains train for every pixel
    	:return: plot trains for each pixel
    	"""
    pixel_x = round(math.sqrt(len(train)))
    fig, axs = plt.subplots(pixel_x, pixel_x)
    k = 0
    for i in range(pixel_x):
        for j in range(pixel_x):
            train[k] = train[k] * synapse[k]
            axs[i, j].stem(train[k])
            k += 1
    fig.suptitle(f"Input: {title}")
    plt.tight_layout()
    plt.show()