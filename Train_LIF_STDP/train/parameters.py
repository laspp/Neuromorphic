################################################ README #########################################################

# This file contains all the parameters of the network.

#################################################################################################################

class old_param:
	scale = 1
	T = 200 # Length of the spike train

	#Neuron
	Prest = 0 # Rest potential of the neuron
	Pth = 50.0*scale # Threshold
	t_ref = 30 # Refractory period
	t_rest = -1
	Pmin = -500.0*scale # Minimum potential
	D = 0.15*scale #Leakage

	t_back = -20
	t_fore = 20

	pixel_x = 28
	
	m = pixel_x*pixel_x #Number of neurons in first layer
	n =  8  #Number of neurons in second layer
	

	# SDPT learning rule
	w_max = 1.5*scale
	w_min = -1.2*scale
	sigma = 0.02
	A_plus = 0.8  # time difference is positive i.e negative reinforcement
	A_minus = 0.3 # 0.01 # time difference is negative i.e positive reinforcement 
	tau_plus = 10
	tau_minus = 10
	
	epoch = 20

	# receptive field
	sca1 =  0.625
	sca2 =  0.125
	sca3 = -0.125
	sca4 = -.5

	# spike train
	a = -1.069
	b = 2.781
	min_Hz = 1
	max_Hz = 20
	norm_freq = 600

	# train
	syn_matrix = 0.4
	syn_winner = 0.06

	# var_th
	norm_th = 3

class new_param:
	scale = 1
	T = 200  # Length of the spike train

	# Neuron
	Prest = 0  # Rest potential of the neuron
	Pth = 30.0 * scale  # Threshold
	t_ref = 30  # Refractory period
	t_rest = -1
	Pmin = -500.0 * scale  # Minimum potential
	D = 0.15 * scale  # Leakage

	t_back = -20
	t_fore = 20

	pixel_x = 2

	m = pixel_x * pixel_x  # Number of neurons in first layer
	n = 2  # Number of neurons in second layer
	#
	# SDPT learning rule
	w_max = 1.5 * scale
	w_min = -1.2 * scale
	sigma = 0.02
	A_plus = 0.8  # time difference is positive i.e negative reinforcement
	A_minus = 0.3  # 0.01 # time difference is negative i.e positive reinforcement
	tau_plus = 10
	tau_minus = 10

	epoch = 30

	# receptive field
	sca1 = 0.625
	sca2 = 0.125
	sca3 = -0.125
	sca4 = -.5

	# spike train
	a = -1.069
	b = 2.781
	min_Hz = 1
	max_Hz = 20
	norm_freq = 600

	# train
	syn_matrix = 0.9			# TODO: menjati ovo
	syn_winner = 0.1			# uvek isti neuron pobedjuje pa zato ovo povecano

	# var_th
	norm_th = 6

class scaling_params:
	scale = 1
	T = 200  # Length of the spike train

	# Neuron
	Prest = 0  # Rest potential of the neuron
	Pth = 50.0 * scale  # Threshold
	t_ref = 30  # Refractory period
	t_rest = -1
	Pmin = -500.0 * scale  # Minimum potential
	D = 0.15 * scale  # Leakage

	t_back = -20
	t_fore = 20

	#pixel_x = 28
	pixel_x = 14

	m = pixel_x * pixel_x  # Number of neurons in first layer
	n = 8  # Number of neurons in second layer

	# SDPT learning rule
	#w_max = 1.5 * scale
	w_max = 0.5 * scale
	w_min = -1.2 * scale
	sigma = 0.02
	A_plus = 0.8  # time difference is positive i.e negative reinforcement
	A_minus = 0.3  # 0.01 # time difference is negative i.e positive reinforcement
	tau_plus = 10
	tau_minus = 10

	epoch = 20

	# receptive field
	sca1 = 0.625
	sca2 = 0.125
	sca3 = -0.125
	sca4 = -.5

	# spike train
	a = -1.069
	b = 2.781
	min_Hz = 1
	max_Hz = 20
	norm_freq = 600

	# train
	syn_matrix = 0.4
	# syn_winner = 0.06
	syn_winner = 0.1

	# var_th
	# norm_th = 3
	norm_th = 7