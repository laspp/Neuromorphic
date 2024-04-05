import random
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def default_params():
    """

    :return: parameters of the model
    """
    params = {}

    # neuron parameters
    params['a'] = 0.02              # timescale of the recovery variable u
    params['b'] = 0.2               # sensitivity of the recovery variable u to the subthreshold fluctuations of the membrane potential v
    params['c'] = -65               # after spike reset value of the membrane potential
    params['d'] = 8                 # after spike reset of the recovery variable u

    params['T'] = 500                 # total duration of simulation
    params['dt'] = 0.1                # simulation time step
    params['range_t'] = np.arange(0, params['T'], params['dt'])          # discrete simulation time

    return params

def run_Izikevic(I_i):
    """
    "Continual" function that describes membrane voltage.
    :param pars: dictionary of parameters
    :param I_i: input current
    :return: voltage of the membrane
    """
    pars = default_params()
    a, b, c, d = pars['a'], pars['b'], pars['c'], pars['d']
    dt, range_t = pars['dt'], pars['range_t']
    v = [c for _ in range(len(range_t))]
    spikes = []
    u = [b*v[j] for j in v]
    #u = [0 for j in v]

    for i in range(len(I_i)-1):

        dv = (0.04*v[i]*v[i] + 5*v[i] + 140 - u[i] + I_i[i])*dt
        v[i+1] = v[i] + dv
        du = a*(b*v[i]-u[i])*dt
        u[i+1] = u[i] + du
        spikes_ms = np.array(spikes)*dt
        if v[i+1]>=30:
            v[i+1] = c

            u[i+1] = u[i+1] + d
            # ovde zabeleziti spajk
            spikes.append(i)
            print("Spike!")
    return v, spikes