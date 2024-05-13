######################################################## README #############################################################

# This file generates rate based spike train from the potential map.

############################################################################################################################


import numpy as np
from numpy import interp
from neuron import neuron
import random
from matplotlib import pyplot as plt
from recep_field import rf
from rl import rl
from rl import update
import math
from parameters import scaling_params as par
#from parameters import new_param as par

def encode(pot):

	#initializing spike train
	train = []
	pixel_x, _ = pot.shape
	for l in range(pixel_x):
		for m in range(pixel_x):
		
			temp = np.zeros([(par.T+1),])

			#calculating firing rate proportional to the membrane potential
			freq = interp(pot[l][m], [par.a, par.b], [par.min_Hz, par.max_Hz])
			#freq = math.ceil(0.102*pot[l][m] + 52.02)
			#print(freq)
			if freq <= 0:
				print("Error frequency <=0")
				
			freq1 = math.ceil(par.norm_freq/freq)

			#generating spikes according to the firing rate
			#print(freq1)
			k = freq1
			if(pot[l][m]>0):
				while k<(par.T+1):
					temp[k] = 1		# visine 1
					k = k + freq1
			train.append(temp)
			# print sum(temp)


	#plot_trains(train, "naslov")


	return train
# lista od 784, nizovi po 201. za svaki piksel vrednost spjkova tj niz od 200
# kao da se slika pokaze na 200ms, pa za svaki piksel ima vrednost u svakoj ms

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
	fig.suptitle(f"Epoch: {title}")
	plt.tight_layout()
	plt.show()


"""
if __name__  == '__main__':
	# m = []
	# n = []
	img = cv2.imread("mnist1/6/" + str(15) + ".png", 0)

	pot = rf(img)

	# for i in pot:
	# 	m.append(max(i))
	# 	n.append(min(i))

	# print max(m), min(n)
	train = encode(pot)
	f = open('look_ups/train6.txt', 'w')
	print np.shape(train)

	for i in range(201):
		for j in range(784):
			f.write(str(int(train[j][i])))
		f.write('\n')

	f.close()
"""