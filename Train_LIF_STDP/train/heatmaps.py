import math
from pprint import pprint

import numpy as np
import seaborn
from matplotlib import pyplot as plt, gridspec
from matplotlib import animation as animation


def rows_cols(elements):
    dict = {1 : (1, 1), 2: (2, 1), 3: (3, 1), 4: (2, 2), 5: (2, 3), 6 : (2, 3), 7: (4, 2), 8: (4, 2),
            9: (3, 3), 10: (3, 4), 11: (3, 4), 12: (3, 4), 13: (3, 5), 14: (3, 5), 15 : (3, 5)}
    rows, cols = dict[elements]
    return rows, cols

def rows_cols2(elements):
    rows = 2
    cols = elements
    return rows, cols

def plotting_potentials(display_plots, ttt, Pth, pot_arrays):
    rows, cols = rows_cols(len(pot_arrays))
    fig, axs = plt.subplots(rows, cols)
    k = 0
    for i in range(rows):
        for j in range(cols):
            if k < len(pot_arrays):
                axs[i, j].set_title(f"Neuron {k}")
                axs[i, j].plot(ttt, Pth, 'r')
                axs[i, j].set_ylim((0 - Pth[0]*0.1), Pth[0]*1.2)
                axs[i, j].plot(ttt, pot_arrays[k])
            else:
                axs[i, j].axis('off')
            k += 1

    if display_plots:
        plt.tight_layout()
        plt.show()
    else:
        plt.close()

def plotting_potentials_and_spikes(display_plots, ttt, Pth, pot_arrays, all_spikes_list):
    rows, cols = rows_cols2(len(pot_arrays))
    fig, axs = plt.subplots(rows, cols)
    k = 0
    for j in range(cols):
        if k < len(pot_arrays):
            axs[0, j].set_title(f"Neuron {k}")
            axs[0, j].plot(ttt, Pth, 'r')
            axs[0, j].set_ylim((0 - Pth[0] * 0.1), Pth[0] * 1.2)
            axs[0, j].plot(ttt, pot_arrays[k])
        else:
            axs[0, j].axis('off')
        k += 1

    k = 0
    for j in range(cols):
        axs[1, j].plot(ttt, all_spikes_list[k], color='b')
        axs[1, j].set_yticks([])
        axs[1, j].set_xticks([])
        axs[1, j].axis('off')
        axs[1, j].set_title(f'Spikes of neuron {j}')
        k+=1

    if display_plots:
        plt.tight_layout()
        plt.show()
    else:
        plt.close()

def synapse_heatmap(synapse, display_plots):
    for i, per_neuron in enumerate(synapse):
        reshape = per_neuron.reshape((int(math.sqrt(synapse)), int(math.sqrt(synapse))))
        seaborn.heatmap(reshape, cmap='Grays')
        if display_plots:
            plt.title(f"Neuron {i}")
            plt.show()
        else:
            plt.close()

def animate_learning(total_syns, display_plots):
    # epoha, inputa, neurona, sinapsi
    rows, cols = rows_cols(total_syns.shape[2])
    fig = plt.figure(figsize=(8, 6))
    ani = animation.FuncAnimation(fig, update_anim, frames=total_syns.shape[0] * total_syns.shape[2], interval=100,
                                  fargs=[total_syns], repeat=False)
    ani.repeat = False
    #writer = animation.ImageMagickWriter(fps=60)
    #ani.save('anim.gif', fps=60)

    #ani.save('anim.gif', writer='ffmpeg', fps=60)

    if display_plots:
        plt.tight_layout()
        plt.show()
        #ani.save('anim.mp4', writer=writer)

    else:
        plt.close()


def update_anim(frame, total_syns):
    plt.clf()
    num_synapses = total_syns.shape[3]
    num_neurons = total_syns.shape[2]
    num_inputs = total_syns.shape[1]
    num_epochs = total_syns.shape[0]
    current_neuron = frame // num_epochs
    current_epoch = frame % num_epochs
    heatmap = plt.imshow(total_syns[current_epoch, ::2, current_neuron, :].reshape((2, 2)), cmap='Purples',
                         interpolation='nearest')
    plt.title(f"Epoch: {current_epoch}, Neuron {current_neuron}")
    plt.colorbar(heatmap)

def plot_trains(train, title, display_plots, synapse=[1, 1, 1, 1]):
    """
    	:param: train is a list (size pixel_x*pixel_x) that contains train for every pixel
    	:return: plot trains for each pixel
    	"""
    rows, cols = rows_cols(len(train))
    fig, axs = plt.subplots(rows, cols)
    k = 0
    for i in range(rows):
        for j in range(cols):
            train[k] = train[k] * synapse[k]
            axs[i, j].stem(train[k])
            k += 1
    fig.suptitle(f"Input: {title}")
    if display_plots:
        plt.tight_layout()
        plt.show()
    else:
        plt.close()