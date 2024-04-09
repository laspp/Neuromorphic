from numpy import *
import numpy as np
import random
from matplotlib import pyplot as plt

N_in = 4   # number of inputs
T = 1.0
dt = 0.01
time  = arange(0, T+dt, dt)

S = [[] for i in range(N_in)]
for j in range(N_in):
    S[j] = []
    for k in range(len(time)):
        r = random.randrange(0,100)
        if r < 5:
            a = 1.0
        else:
            a = 0.0
        # a = 0.1 # in case of constant input
        S[j].append(a)
print(S)

w = [5.0, 10.0, 20.0, 30.0] # weights
v = zeros(len(time))    # membrane potential

v_rest = 0
Thr = 3
R = 0.5
C = 0.2
t_ref = 0.1
t_rest = 0 

I = []  # weighted sum of inputs
for i, t in enumerate(time):
    #print(i, t)
    suma = 0
    for j in range(N_in):
        suma = suma + w[j]*S[j][i]
    I.append(suma)
    
    if t <= t_rest:
        v[i] = v_rest
    elif t > t_rest:
        v[i] = v[i-1] + (-v[i-1]/(R*C) + I[i]/C)*dt
            
    if v[i] >= Thr:
        v[i] = Thr  # it falls after that
        t_rest = t + t_ref

print(v, I)

#--- Plot
tt = arange(0,len(v),1)
axes = plt.gca()
axes.set_ylim([-1,4])
I_C = [i/C*dt for i in I]
plt.plot(tt,[Thr for i in I])
plt.plot(tt,I_C)
plt.plot(tt,v)
plt.show()

