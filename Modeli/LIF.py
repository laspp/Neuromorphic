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
    params['V_th'] = -55              # treshold value, [mV]
    params['V_reset'] = -65           # reset potential [mV]
    params['tau'] = 10                # tau = RC [ms]
    params['R'] = 1 / 10                # nano oma      TODO: zasto 'nano' a ne 'mili' jedinica?
    params['V_init'] = -65
    params['V_rest'] = -65            # equilibrium point, [mV]
    params['tref'] = 5                # refractory period, [ms]

    params['T'] = 500                 # total duration of simulation
    params['dt'] = 0.1                # simulation time step

    params['range_t'] = np.arange(0, params['T'], params['dt'])          # discrete simulation time

    return params

def run_LIF(pars, I_i):
    """
    "Continual" function that describes membrane voltage.
    :param pars: dictionary of parameters
    :param I_i: input current
    :return: voltage of the membrane
    """
    V_th, V_rest, V_init = pars['V_th'], pars['V_rest'], pars['V_init']
    tau, R = pars['tau'], pars['R']
    C = tau / R
    dt, range_t, tref = pars['dt'], pars['range_t'], pars['tref']
    v = [0 for _ in range(len(range_t))]
    v[0] = V_rest
    spikes = []
    tr = 0          # count for refractory duration
    flag_th = False

    for i in range(len(range_t)-1):
        if flag_th:
            v[i] = V_rest
            flag_th = False

        if tr>0:                # still in refractory period
            v[i] = V_rest
            tr = tr - 1

        elif v[i] > V_th:
            flag_th = True
            spikes.append(i)
            v[i] = V_th
            #v[i] = V_rest
            tr = tref/dt            # entering refractory time

        dv = (-v[i] + R*I_i[i] + V_rest) * dt * (1/tau)
        v[i+1] = v[i] + dv
        spikes_ms = np.array(spikes)*dt
    return v, spikes

def run_disc_LIF():
    pass

def generate_delta(no, range_t):
    """
    Generation of delta current input.
    :param no: number of nonzero values
    :param range_t: full time range
    :return: delta impulse, array
    """
    I_delta = np.zeros(len(range_t))            # array of 0
    # for i in range(0, no):
    #     rand_idex = random.randint(0, len(range_t) - 1)
    #     I_delta[rand_idex] = random.randint(2000, 50000)
    no = 30
    for i in range(0, no):
        distance = int(len(range_t)/no)
        print(distance)
        I_delta[distance*i] = 9000

    # I_delta[100] = 5000
    # I_delta[150] = 5000
    # I_delta[200] = 5000
    # I_delta[250] = 5000
    # I_delta[2000] = 5000

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
    V_th = pars['V_th']
    range_t = pars['range_t']
    ax.plot(range_t, v, label='membrane_voltage', color='blue')
    ax.tick_params(axis='y')
    ax.axhline(V_th, ls='--', color='blue')
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
I_const = 105 * np.ones(len(p['range_t']))
NO = 4
I_delta = generate_delta(NO, p['range_t'])

v, spikes_ms = run_LIF(p, I_const)
fig, axs = plt.subplots(3, sharex=True, sharey=False)
plot_input(axs[0], I_const, p['range_t'])
plot_voltage(axs[1], p, v)
ax2 = plot_spikes(axs[2], spikes_ms, p['range_t'])

plt.show()

v2, spikes_ms2 = run_LIF(p, I_delta)
fig, axs = plt.subplots(3, sharex=True, sharey=False)
plot_input(axs[0], I_delta, p['range_t'])
plot_voltage(axs[1], p, v2)
ax2 = plot_spikes(axs[2], spikes_ms2, p['range_t'])
plt.show()


spikes_ms2 = [item * p['dt'] for item in spikes_ms2]
print(f"Spikes at: {spikes_ms2} ms")




#print(v)
