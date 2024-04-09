from model import neuron

input_n = 4
ms = 1000
spike_train_black = [1 if i%100==0 else 0 for i in range(ms)]
spike_train_white = [1 if i%300==0 else 0 for i in range(ms)]
I = [1 for _ in range(1000)]
print(I)
eq_input = neuron.run_Izikevic(I)                  # TODO: sta ce biti struja I

input_layer = []
for i in range(input_n):
    input_layer.append(neuron.run_Izikevic(I))

# sinapse