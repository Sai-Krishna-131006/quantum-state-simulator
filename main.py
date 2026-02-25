import numpy as np
import matplotlib .pyplot as plt 

#--computational basis--#
zero = np.array([[1], [0]])
one = np.array([[0], [1]])

#--arbitrary state--#
psi = np.array([[3],[4]])

#--normalization--#
norm = np.sqrt(np.conjugate(psi.T)@psi)
psi = psi / norm

print('Normalized state')
print(psi)

#--projection operators--#
P0 = zero@np.conjugate(zero.T)
P1 = one@np.conjugate(one.T)

#--born rule probabilities--#
prob0 = (np.conjugate(psi.T)@P0@psi).real.item()
prob1 = (np.conjugate(psi.T)@P1@psi).real.item()

print('Probability of state |0> - ',prob0)
print('Probability of state |1> - ',prob1)
print('Sum - ',prob0+prob1)  #Should give one



states = ['|0>', '|1>']
probs = [prob0, prob1]

plt.bar(states, probs)
plt.ylim(0,1)
plt.title("Measurement Probabilities")
plt.ylabel("Probability")
plt.show()