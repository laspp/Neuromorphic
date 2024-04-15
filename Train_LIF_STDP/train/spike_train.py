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
from parameters import param as par

def encode(pot):

	#initializing spike train
	train = []

	for l in range(par.pixel_x):
		for m in range(par.pixel_x):
		
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
	return train
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