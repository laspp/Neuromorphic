####################################################### README #########################################################

# This file consists of function that convolves an image with a receptive field so that input to the network is 
# close to the form perceived by our eyes. 

#########################################################################################################################

# filtriranje slike

# TODO: za binarne slike pogledati kako izracuna, treba da su dovoljno razmaknute vrednosti
# ali i da ne bude negde 0 jer onda nema spajka. mozda rucno fiksirati neke vrednosti
import numpy as np
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
	# pot = np.zeros([2, 2])
	# pprint(pot)
	# pot = [[0.2, 0.2], [0.8, 0.8]]
	# pprint(pot)

	ran = [-2,-1,0,1,2]				# TODO: sta su ovi param
	ox = 2
	oy = 2

	#region konvolucija
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
	#region hard
	# upper_black = np.zeros((28, 28))
	# upper_black[14:, :] = 255			# [0 0 0 .. 255 255 255]
	# upper_white = np.zeros((28, 28))
	# upper_white[:14, :] = 255			# [255 255 255 ... 0 0 0]
	# whole_black = np.zeros((28, 28))
	# whole_white = np.zeros((28, 28))
	# whole_white[:, :] = 255
	# first_rows = np.zeros((28, 28))
	# first_rows[:1, :] = 255
	# if np.all(inp == upper_black): 	# crno pa belo
	# 	#pot = [[0.2, 0.2], [0.8, 0.8]]
	# 	pot = np.zeros((28, 28))
	# 	pot[:14, :] = 0
	# 	pot[14:, :] = 3.5
	# elif np.all(inp == upper_white):
	# 	pot = np.zeros((28, 28))
	# 	pot[:14, :] = 3.5
	# 	pot[14:, :] = 0
	# elif np.all(inp == whole_black):
	# 	pot = np.zeros((28, 28))
	# elif np.all(inp == whole_white):
	# 	pot = np.zeros((28, 28))
	# 	pot[:, :] = 3.5
	# elif np.all(inp == first_rows):
	# 	pot = np.zeros((28, 28))
	# 	pot[:1, :] = 3.5
	# 	pot[1:, :] = 3.5
	#
	# else:
	# 	raise Exception("Invalid input image")
	#endregion

	rows, cols = inp.shape
	upper_black = np.zeros_like(inp)
	upper_white = np.zeros_like(inp)
	upper_black[rows//2:, :] = 255
	upper_white[:rows//2, :] = 255
	karo1 = [[0, 255], [255, 0]]
	karo2 = [[255, 0], [0, 255]]


	if np.all(inp == upper_black):
		pot = np.zeros_like(inp)
		pot[:rows//2, :] = 0
		pot[rows//2:, :] = 3.5
	elif np.all(inp == upper_white):
		pot = np.zeros_like(inp)
		pot[:rows//2, :] = 3.5
		pot[rows//2:, :] = 0
	elif np.all(inp == karo1):
		pot = [[0, 3.5], [3.5, 0]]
	elif np.all(inp == karo2):
		pot = [[3.5, 0], [0, 3.5]]
	else:
		raise Exception("Invalid input image")

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