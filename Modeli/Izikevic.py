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
    #u = [0 for j in v]

    for i in range(len(range_t)-1):

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

def generate_const_I(intensity):
    I_const = intensity * np.ones(len(p['range_t']))
    return I_const

def generate_r_delta(no, range_t, max_intensity):
    """
    Generation of delta current input.
    :param no: number of nonzero values
    :param range_t: full time range
    :return: delta impulse, array
    """
    I_delta = np.zeros(len(range_t))            # array of 0
    for i in range(0, no):
        rand_idex = random.randint(0, len(range_t) - 1)
        I_delta[rand_idex] = random.randint(1, max_intensity)

    I_delta[10] = 18
    I_delta[11] = 18
    I_delta[12] = 18
    I_delta[13] = 18


    I_delta[15] = 18
    I_delta[16] = 18
    I_delta[17] = 18
    I_delta[18] = 18


    I_delta[20] = 18
    I_delta[21] = 18
    I_delta[22] = 18
    I_delta[23] = 18

    I_delta[25] = 18
    I_delta[26] = 18
    I_delta[27] = 18
    I_delta[28] = 18


    #I_delta[800] = 50

    return I_delta

def generate_eqv_delta(no, range_t, intensity):
    I_delta = np.zeros(len(range_t))
    # ako ima 5000 na 5 to je na svakih 1000
    delovi = int(len(range_t)/no)
    for i in range(0, no):
        I_delta[i*delovi] = intensity
    I_delta[0] = 0
    return I_delta

def generate_heviside(no, range_t, duration, intensity):
    I_heviside = np.zeros(len(range_t))
    delovi = int(len(range_t)/no)
    for i in range(no):
        for j in range(duration):
            I_heviside[i*delovi + j] = intensity
    I_heviside[0] = 0
    return I_heviside


def plot_input(ax, I, range):
    """
    Plots input current.
    :param I: input current
    :param range: full time range
    :param title:
    :return: plot
    """
    ax.set_ylabel('I [mA]')
    ax.plot(range, I, label='I', color='green')
    ax.tick_params(axis='y')
    ax.set_title('Input current')
    ax.set_ylim(bottom=-0.01)
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
NO = 8
intensity_const = 0
intensity_delta = 20
intensity_eqv = 20
intensity_heviside = 20
heviside_duration = 20          #[ms]
I_const = generate_const_I(intensity_const)
I_delta = generate_r_delta(NO, p['range_t'], intensity_delta)
I_eqv = generate_eqv_delta(NO, p['range_t'], intensity_eqv)
I_heviside = generate_heviside(NO, p['range_t'], heviside_duration, intensity_heviside)

v, spikes_ms = run_Izikevic(p, I_const)
fig, axs = plt.subplots(3, sharex=True, sharey=False)
plot_input(axs[0], I_const, p['range_t'])
plot_voltage(axs[1], p, v)
ax2 = plot_spikes(axs[2], spikes_ms, p['range_t'])

plt.show()

v2, spikes2 = run_Izikevic(p, I_delta)
fig, axs = plt.subplots(3, sharex=True, sharey=False)
plot_input(axs[0], I_delta, p['range_t'])
plot_voltage(axs[1], p, v2)
ax2 = plot_spikes(axs[2], spikes2, p['range_t'])
plt.show()

print(f"Spikes {spikes2}")
spikes_ms2 = [item * p['dt'] for item in spikes2]
print(f"Spikes at: {spikes_ms2} ms")

v3, spikes3 = run_Izikevic(p, I_eqv)
fig, axs = plt.subplots(3, sharex=True, sharey=False)
plot_input(axs[0], I_eqv, p['range_t'])
plot_voltage(axs[1], p, v3)
ax2 = plot_spikes(axs[2], spikes3, p['range_t'])
plt.show()


v4, spikes4 = run_Izikevic(p, I_heviside)
fig, axs = plt.subplots(3, sharex=True, sharey=False)
plot_input(axs[0], I_heviside, p['range_t'])
plot_voltage(axs[1], p, v4)
ax2 = plot_spikes(axs[2], spikes4, p['range_t'])
plt.show()




#print(v)
