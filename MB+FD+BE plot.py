import numpy as np
import matplotlib.pyplot as plt

#Parameters
k = 8.617*10**(-5) #eV/K, found this on google 
E = np.linspace(0, 0.5, 1000)  # eV
mu = 0.5  # eV for FD

# Maxwell-Boltzmann
def f_mb(E, T): 
    return (2 / np.sqrt(np.pi)) * (1/(k*T))**1.5 * np.sqrt(E) * np.exp(-E/(k*T))

# Fermi-Dirac
def f_fd(E, T):
    kT = k * T
    return 1 / (np.exp((E - mu)/kT) + 1)

# Bose-Einstein
def f_be(E, T):
    kT = k * T
    return 1 / (np.exp(E/kT) - 1)

#plot of Maxwell Boltzman
plotfmb1 = f_mb(E, 600)
plotfmb2 = f_mb(E, 800)
plotfmb3 = f_mb(E, 1200)
plotfmb4 = f_mb(E, 1600)

plt.figure(figsize=(10,7))
plt.plot(E, plotfmb1,label='600k')
plt.plot(E, plotfmb2,label='800k')
plt.plot(E, plotfmb3,label='1200k')
plt.plot(E, plotfmb4,label='1600k')
plt.grid()
plt.xlabel('ev')
plt.ylabel('f(E)')
plt.title('Maxwell-Boltzman Distribution')
plt.legend()
plt.show()

#plot of Fermi Dirac
plotffd1 = f_fd(E, 600)
plotffd2  = f_fd(E, 800)
plotffd3  = f_fd(E, 1200)
plotffd4  = f_fd(E, 1600)

plt.figure(figsize=(10,7))
plt.plot(E, plotffd1,label='600k')
plt.plot(E, plotffd2,label='800k')
plt.plot(E, plotffd3,label='1200k')
plt.plot(E, plotffd4,label='1600k')
plt.xlabel('ev')
plt.ylabel('f(E)')
plt.title('Fermi-Dirac Distribution')
plt.grid()
plt.legend()
plt.show()

#plot of Bose Einstein
plotfbe1 = f_be(E, 600)
plotfbe2  = f_be(E, 800)
plotfbe3  = f_be(E, 1200)
plotfbe4  = f_be(E, 1600)

plt.figure(figsize=(10,7))
plt.plot(E, plotfbe1,label='600k')
plt.plot(E, plotfbe2,label='800k')
plt.plot(E, plotfbe3,label='1200k')
plt.plot(E, plotfbe4,label='1600k')
plt.grid()
plt.xlabel('ev')
plt.ylabel('f(E)')
plt.yscale('log')
plt.title('Bose-Einstein Distribution')
plt.legend()
plt.show()

