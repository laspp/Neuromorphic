################################################ README #########################################################

# This file contains all the parameters of the network.

#################################################################################################################

class param:
	scale = 1
	T = 200 # Length of the spike train

	#Neuron
	Prest = 0 # Rest potential of the neuron
	Pth = 50.0*scale # Threshold
	t_ref = 30 # Refractory period
	Pmin = -500.0*scale # Minimum potential
	D = 0.15*scale #Leakage

	t_back = -20
	t_fore = 20

	pixel_x = 28
	
	m = pixel_x*pixel_x #Number of neurons in first layer
	n =  8  #Number of neurons in second layer
	
	# 
	
	w_max = 1.5*scale
	w_min = -1.2*scale
	sigma = 0.02
	A_plus = 0.8  # time difference is positive i.e negative reinforcement
	A_minus = 0.3 # 0.01 # time difference is negative i.e positive reinforcement 
	tau_plus = 10
	tau_minus = 10
	
	epoch = 20