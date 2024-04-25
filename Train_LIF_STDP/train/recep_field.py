####################################################### README #########################################################

# This file consists of function that convolves an image with a receptive field so that input to the network is 
# close to the form perceived by our eyes. 

#########################################################################################################################

# filtriranje slike

# TODO: za binarne slike pogledati kako izracuna, treba da su dovoljno razmaknute vrednosti
# ali i da ne bude negde 0 jer onda nema spajka. mozda rucno fiksirati neke vrednosti
import numpy as np
from numpy import interp

from parameters import scaling_params as par
#from parameters import new_param as par				# for 2x2 image
from pprint import pprint

def rf(inp):
	"""
	:param inp: input image, as a matrix
	:return:
	"""
	sca1 = par.sca1
	sca2 = par.sca2
	sca3 = par.sca3
	sca4 = par.sca4

	#Receptive field kernel
	w = [[	sca4 ,sca3 , sca2 ,sca3 ,sca4],
	 	[	sca3 ,sca2 , sca1 ,sca2 ,sca3],
	 	[ 	sca2 ,sca1 , 	1 ,sca1 ,sca2],
	 	[	sca3 ,sca2 , sca1 ,sca2 ,sca3],
	 	[	sca4 ,sca3 , sca2 ,sca3 ,sca4]]

	pot = np.zeros([par.pixel_x,par.pixel_x])



	#region konvolucija
	# ran = [-2,-1,0,1,2]
	# ox = 2
	# oy = 2
	# Convolution
	# smoothing
	# for i in range(par.pixel_x):
	# 	for j in range(par.pixel_x):
	# 		summ = 0
	# 		for m in ran:
	# 			for n in ran:
	# 				if (i+m)>=0 and (i+m)<=par.pixel_x-1 and (j+n)>=0 and (j+n)<=par.pixel_x-1:
	# 					summ = summ + w[ox+m][oy+n]*inp[i+m][j+n]/255
	# 		pot[i][j] = summ
	#endregion



	for i in range(par.pixel_x):
		for j in range(par.pixel_x):
			if inp[i][j] == 0:
				pot[i][j] = 0
			elif inp[i][j] == 255:
				pot[i][j] = 3.5
			else:
				pot[i][j] = int(interp(inp[i][j], [0, 255], [0, 3.5]))
				#raise Exception("Siva")

	#print(pot)
	return pot			# treba da bude ndarray (28, 28), odnosno (2, 2)

# upper_black = np.zeros((28, 28))
# upper_black[14:, :] = 255			# [0 0 0 .. 255 255 255]
# rf(upper_black)
"""
if __name__ == '__main__':

	img = cv2.imread("mnist1/" + str(1) + ".png", 0)
	pot = rf(img)
	max_a = []
	min_a = []
	for i in pot:
		max_a.append(max(i))
		min_a.append(min(i))
	print "max", max(max_a)
	print "min", min(min_a)
"""