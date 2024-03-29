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
    params['dt'] = 0.5                # simulation time step
    params['range_t'] = np.arange(0, params['T'], params['dt'])          # discrete simulation time

    return params

def run_Izikevic(pars, I_i):
    """
    "Continual" function that describes membrane voltage.
    :param pars: dictionary of parameters
    :param I_i: input current
    :return: voltage of the membrane
    """
    a, b, c, d = pars['a'], pars['b'], pars['c'], pars['d']
    dt, range_t = pars['dt'], pars['range_t']
    v = [c for _ in range(len(range_t))]
    spikes = []
    u = [b*v[j] for j in v]

    for i in range(len(range_t)-1):

        dv = (0.04*v[i]*v[i] + 5*v[i] + 140 - u[i] + I_i[i])*dt
        v[i+1] = v[i] + dv
        du = a*(b*v[i]-u[i])*dt
        u[i+1] = u[i] + du
        spikes_ms = np.array(spikes)*dt
        if v[i]>=30:                            # TODO: v[i] ili v[i+1]
            v[i] = c
            u[i] = u[i] + d
            # ovde zabeleziti spajk
    return v, spikes


def generate_delta(no, range_t):
    """
    Generation of delta current input.
    :param no: number of nonzero values
    :param range_t: full time range
    :return: delta impulse, array
    """
    I_delta = np.zeros(len(range_t))            # array of 0
    for i in range(0, no):
        rand_idex = random.randint(0, len(range_t) - 1)
        I_delta[rand_idex] = random.randint(1, 50)

    I_delta[10] = 50
    I_delta[15] = 50
    I_delta[20] = 50
    I_delta[25] = 50
    I_delta[800] = 50

    return I_delta

# napraviti diskretno, kao za digitalna kola
# broj bitova parametar
# library za diskretizaciju

def plot_input(ax, I, range):
    """
    Plots input current.
    :param I: input current
    :param range: full time range
    :param title:
    :return: plot
    """
    ax.set_ylabel('I')
    ax.plot(range, I, label='I', color='green')
    ax.tick_params(axis='y')
    ax.set_title('Input current')
    return ax

    # plt.plot(range, I)
    # plt.title(title)
    # plt.show()


def plot_voltage(ax, pars, v):
    """

    :param pars: parameter dictionary
    :param v: voltage
    :param sp: spike train
    :return: figure of the membrane potential
    """

    ax.set_ylabel('V [mV]', color='blue')
    range_t = pars['range_t']
    ax.plot(range_t, v, label='membrane_voltage', color='blue')
    ax.tick_params(axis='y')
    ax.set_title("Membrane voltage")
    return ax

def plot_spikes(ax, sp, range):
    """

    :param sp: array of spikes
    :param range: time range
    :return: figure of spikes
    """
    spikes = np.zeros(len(range))
    for i in sp:
        spikes[i] = 1

    ax.set_xlabel('Time [ms]')
    ax.set_ylabel('Spikes', color='orange')
    ax.plot(range, spikes, label='spikes', color='orange')
    ax.tick_params(axis='y', labelcolor='orange')
    ax.set_yticks(np.arange(0, 1.5, 1))
    ax.set_title('Spikes')
    return ax


p = default_params()
I_const = 1 * np.ones(len(p['range_t']))
NO = 4
I_delta = generate_delta(NO, p['range_t'])

v, spikes_ms = run_Izikevic(p, I_const)
fig, axs = plt.subplots(3, sharex=True, sharey=False)
plot_input(axs[0], I_const, p['range_t'])
plot_voltage(axs[1], p, v)
ax2 = plot_spikes(axs[2], spikes_ms, p['range_t'])

plt.show()

v2, spikes_ms2 = run_Izikevic(p, I_delta)
fig, axs = plt.subplots(3, sharex=True, sharey=False)
plot_input(axs[0], I_delta, p['range_t'])
plot_voltage(axs[1], p, v2)
ax2 = plot_spikes(axs[2], spikes_ms2, p['range_t'])
plt.show()


spikes_ms2 = [item * p['dt'] for item in spikes_ms2]
print(f"Spikes at: {spikes_ms2} ms")




#print(v)
