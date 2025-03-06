import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as sc

e = 1  
k_B = sc.Boltzmann

T = np.linspace(0.1, 5, 100)
beta = 1/T  
def Z(beta, N):
    
    return (np.exp(-beta*e) + np.exp(-2*beta*e))**N
Z1 = np.exp(-beta*e) + np.exp(-2*beta*e)  #partition function
U1 = (e*np.exp(-beta*e) + 2*e*np.exp(-2*beta*e)) / Z1  # Energy per particle

Ns = [1, 2, 10]
qnt = {
    'U': [N*U1 for N in Ns],
    'Delta E': [N*( (e**2*np.exp(-beta*e) + (2*e)**2*np.exp(-2*beta*e))/Z1 - U1**2 ) for N in Ns],
    'C': [N*( ( (e**2*np.exp(-beta*e) + (2*e)**2*np.exp(-2*beta*e))/Z1 - U1**2 ) * beta**2 ) for N in Ns],
    'F': [-(1/beta)*np.log(Z(beta, N)) for N in Ns],
    'S': [(N*U1 + (1/beta)*np.log(Z(beta, N))) * beta for N in Ns]
}


for name, values in qnt.items():
    plt.figure(figsize=(10, 7))
    for i, N in enumerate(Ns):
        plt.plot(T, values[i], label=f'N={N}')
    plt.xlabel('Temperature (T)')
    plt.ylabel(name)
    plt.legend()
    plt.grid()
    plt.show()


plow = np.exp(-beta*e)/Z1
phigh = np.exp(-2*beta*e)/Z1

plt.figure(figsize=(10, 7))
plt.plot(T, plow, label='p(E)')
plt.plot(T, phigh, label='p(2E)')
plt.xlabel('Temperature (T)')
plt.ylabel('Occupation Probability')
plt.legend()
plt.grid()
plt.show()