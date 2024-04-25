###################################################### README #####################################################

# This file is used to leverage the generative property of a Spiking Neural Network. reconst_weights function is used
# for that purpose. Looking at the reconstructed images helps to analyse training process.

####################################################################################################################


import numpy as np
from numpy import interp
from recep_field import rf
from parameters import scaling_params as par
import os
#from parameters import new_param as par
import cv2


def reconst_weights(weights, num):
	weights = np.array(weights)
	weights = np.reshape(weights, (par.pixel_x,par.pixel_x))
	img = np.zeros((par.pixel_x,par.pixel_x))
	for i in range(par.pixel_x):
		for j in range(par.pixel_x):
			img[i][j] = int(interp(weights[i][j], [par.w_min,par.w_max], [0,255]))
			#img[i][j] = int(interp(weights[i][j], [-1.2, 1], [0, 255]))
			# DONE: skaliranje!!
	#cv2.imwrite('neuron' + str(num) + '.png' ,img)
	output_dir = os.path.join(os.path.dirname(__file__), '..', 'reconstructs')

	#cv2.imwrite('neuron' + str(num-1) + '.png' ,img)
	cv2.imwrite(os.path.join(output_dir, 'neuron' + str(num - 1) + '.png'), img)

	return img

"""
if __name__ == '__main__':

	img = cv2.imread("images2/" + "69" + ".png", 0)
	pot = rf(img)
	reconst_rf(pot, 12)
"""