# ovo je main
from pprint import pprint

####################################################### README ####################################################################

# This is the main file which calls all the functions and trains the network by updating weights


#####################################################################################################################################

import numpy as np
import seaborn as seaborn

from heatmaps import *
from neuron import neuron
import random
from matplotlib import pyplot as plt
import cv2
from recep_field import rf
from spike_train import encode, plot_trains
from rl import rl
from rl import update
from reconstruct import reconst_weights
from parameters import scaling_params as par
from var_th import threshold
import os
import sys
from pathlib import Path


def train_net(train_data_dir, pixel_x, display_plots=False):
	#potentials of output neurons
	pot_arrays = []
	for i in range(par.n):
		pot_arrays.append([])

	#time series
	time = np.arange(1, par.T+1, 1)

	layer2 = []

	# creating the hidden layer of neurons
	for i in range(par.n):
		a = neuron()
		layer2.append(a)

	#synapse matrix	initialization
	synapse = np.zeros((par.n, pixel_x*pixel_x))
	print(type(synapse))

	for i in range(par.n):
		for j in range(pixel_x*pixel_x):
			#random.seed(1)
			synapse[i][j] = random.uniform(0, par.syn_matrix*par.scale)
			# TODO: napraviti poznate sinapse, fiksne izmedju 0 i 0.4
			#synapse[i][j] = j/10 + 0.1

	pprint("Prvobitne sinapse")
	pprint(synapse)


	per_file = np.zeros((2, par.n, pixel_x*pixel_x))
	total_syns = np.zeros((par.epoch, 2, par.n, pixel_x*pixel_x))
	print(f"Oblik per file {np.shape(per_file)}")
	print(f"Oblik total syns {np.shape(total_syns)}")

	# (epoha, slika, neurona, piksela)
	for k in range(par.epoch):
		print("EPOCH", k,":")
		last_winners = {}
		all_trains = []
		per_file = np.zeros((2, par.n, pixel_x*pixel_x))
		for i, file in enumerate(os.listdir(train_data_dir)):

			if file.endswith('.png'):
				image = cv2.imread(os.path.join(train_data_dir, file), 0)
				#Convolving image with receptive field
				pot = rf(image)
				#pot=image/255
				#print(pot)				# 28x28
				#Generating spike train
				train = np.array(encode(pot))	#784x201
				all_trains.append(train)
				#calculating threshold value for the image
				var_threshold = threshold(train)

				# print var_threshold
				# synapse_act = np.zeros((par.n,par.m))
				# var_threshold = 9
				# print var_threshold
				#var_D = (var_threshold*3)*0.07

				for x in layer2:
					x.initial(var_threshold)

				#flag for lateral inhibition
				f_spike = 0

				img_win = None

				active_pot = []
				for index1 in range(par.n):
					active_pot.append(0)

				#Leaky integrate and fire neuron dynamics
				for t in time:
					for j, x in enumerate(layer2):
						active = []
						if(x.t_rest<t):
							x.P = x.P + np.dot(synapse[j], train[:,t])
							if(x.P>par.Prest):
								x.P -= par.D			#leak
							active_pot[j] = x.P

						pot_arrays[j].append(x.P)

					# Lateral Inhibition
					if(f_spike==0):
						high_pot = max(active_pot)
						if(high_pot>var_threshold):
							f_spike = 1
							winner = np.argmax(active_pot)
							img_win = winner
							print(file," -> " ," Neuron ",str(winner))
							last_winners[file] = winner
							for s in range(par.n):
								if(s!=winner):
									layer2[s].P = par.Pmin			#ugasi ostale

					#Check for spikes and update weights
					for j,x in enumerate(layer2):
						s = x.check()
						if(s==1):
							x.t_rest = t + x.t_ref
							x.P = par.Prest
							for h in range(pixel_x*pixel_x):
								for t1 in range(-2,par.t_back-1, -1):
									if 0<=t+t1<par.T+1:
										if train[h][t+t1] == 1:
											print("1: weight change by" + str(update(synapse[j][h], rl(t1))))
											synapse[j][h] = update(synapse[j][h], rl(t1))




								for t1 in range(2,par.t_fore+1, 1):
									if 0<=t+t1<par.T+1:
										if train[h][t+t1] == 1:
											print("2: weight change by" + str(update(synapse[j][h], rl(t1))))
											synapse[j][h] = update(synapse[j][h], rl(t1))

				if(img_win):
					for p in range(pixel_x*pixel_x):
						if sum(train[p])==0:
							synapse[img_win][p] -= par.syn_winner*par.scale			# da u sl iteraciji i drugi mogu da pobede
							if(synapse[img_win][p]<par.w_min):
								synapse[img_win][p] = par.w_min
				per_file[i] = synapse


		total_syns[k] = per_file

	print(f"Oblik per file posle svih epoha {np.shape(per_file)}")
	print(f"Oblik total syns posle svih epoha {np.shape(total_syns)}")
	pprint(total_syns)

	animate_learning(total_syns)





	#print(last_winners)

	ttt = np.arange(0,len(pot_arrays[0]),1)
	Pth = []
	for i in range(len(ttt)):
		Pth.append(layer2[0].Pth)

	# plotting neuron active potentials
	#plotting_potentials(display_plots, ttt, Pth, pot_arrays)



	seaborn.heatmap(synapse)
	if display_plots:
		plt.title("Svee")
		plt.show()

	synapse_heatmap(synapse, display_plots)


	for item in all_trains:
		#print(f"All trains {np.shape(all_trains)}")
		#print(f"Item {np.shape(item)}")

		#plot_trains(item, f"kraj, neuron {i}", synapse[i])
		pass
	#plot_trains(all_trains[0], f"kraj, 0.png, neuron {i}", synapse[i])
	#plot_trains(all_trains[1], f"kraj, 1.png, neuron {i}", synapse[i])
		# TODO: sacuvati to u neki fajl
		# HEAT MAP, 9 NEURONA, po sinapsama, po bojama
	# moze animacija iz pocetnih sinapsi do kraja svih epoha
	# matplotlib animation




	#Reconstructing weights to analyse training
	for i in range(par.n):
		reconst_weights(synapse[i], i, pixel_x)



	return synapse, last_winners

# Defining main function
def main(data_path=None, *other):
	if other:
		print(("Wrong number of arguments! {} given.\n"
			   "Run:  python train.py [path to train data]\n").format(len(other)))
		exit()
	#Use default data set if no data given
	if not data_path:
		base_path = Path(__file__).parent.parent
		print(base_path)
		#data_path = Path(base_path, 'data', 'MNIST_0-5')
		data_path = Path(base_path, 'data', 'TOY_BINARY')
		#data_path = Path(base_path, 'data', 'BINARY_14')
		#data_path = Path(base_path, 'data', 'MNIST_TRAIN')


	print("Using training data in folder: ",data_path)
	image_file = next(data_path.glob('*.png'), None)
	img = cv2.imread(str(image_file))
	pixel_x, _, _ = img.shape

	train_net(data_path, pixel_x)
	return data_path



# Using the special variable
# __name__ 
if __name__=="__main__":
	main(*sys.argv[1:])

# TODO: staviti fiksne tezine sinapsi pa da se spajkuju za odgovarajuce slike
