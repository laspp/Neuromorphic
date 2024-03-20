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

    for i in range(len(range_t)-1):

        if tr>0:                # still in refractory period
            v[i] = V_rest
            tr = tr - 1

        elif v[i] > V_th:
            spikes.append(i)
            v[i] = V_rest
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
    for i in range(0, no):
        rand_idex = random.randint(0, len(range_t) - 1)
        I_delta[rand_idex] = random.randint(5000, 50000)
    I_delta[110] = 5000
    I_delta[130] = 5000
    I_delta[150] = 5000
    I_delta[170] = 5000

    return I_delta

# napraviti diskretno, kao za digitalna kola
# broj bitova parametar
# library za diskretizaciju

def plot_input(I, range, title):
    """
    Plots input current.
    :param I: input current
    :param range: full time range
    :param title:
    :return: plot
    """
    plt.plot(range, I)
    plt.title(title)
    plt.show()


def plot_voltage(pars, v, title):
    """

    :param pars: parameter dictionary
    :param v: voltage
    :param sp: spike train
    :return: figure of the membrane potential
    """

    fig, ax1 = plt.subplots()
    ax1.set_xlabel('Time [ms]')
    ax1.set_ylabel('V [mV]', color='blue')


    V_th = pars['V_th']
    T = pars['T']
    range_t = pars['range_t']
    ax1.plot(range_t, v, label='membrane_voltage', color='blue')
    ax1.tick_params(axis='y')
    ax1.axhline(V_th, ls='--', color='blue')
    return ax1

def plot_spikes(sp, range):
    """

    :param sp: array of spikes
    :param range: time range
    :return: figure of spikes
    """
    spikes = np.zeros(len(range))
    for i in sp:
        spikes[i] = 1


    ax2 = plt.gca().twinx()
    ax2.set_ylabel('Spikes', color='orange')
    ax2.plot(range, spikes, label='spikes', color='orange')
    ax2.tick_params(axis='y', labelcolor='orange')
    ax2.set_yticks(np.arange(0, 1.5, 1))
    return ax2


p = default_params()
I_const = 105 * np.ones(len(p['range_t']))
NO = 4
I_delta = generate_delta(NO, p['range_t'])

v, spikes_ms = run_LIF(p, I_const)
plot_input(I_const, p['range_t'], "Constant input current")
ax1 = plot_voltage(p, v, ", constant input current")
ax2 = plot_spikes(spikes_ms, p['range_t'])
plt.title("Constant input current")
legend_patches = [
    mpatches.Patch(color='tab:blue', label='membrane voltage'),
    mpatches.Patch(color='tab:orange', label='spikes')
]

# Add legend with custom handles and labels
plt.legend(handles=legend_patches)
plt.show()


v2, spikes_ms2 = run_LIF(p, I_delta)
plot_input(I_delta, p['range_t'], "Delta input current")
ax1 = plot_voltage(p, v2, ", delta input current")
ax2 = plot_spikes(spikes_ms2, p['range_t'])
plt.title("Delta input current")
legend_patches = [
    mpatches.Patch(color='tab:blue', label='membrane voltage'),
    mpatches.Patch(color='tab:orange', label='spikes')
]

# Add legend with custom handles and labels
plt.legend(handles=legend_patches)
plt.show()

spikes_ms2 = [item * p['dt'] for item in spikes_ms2]
print(f"Spikes at: {spikes_ms2} ms")




#print(v)
