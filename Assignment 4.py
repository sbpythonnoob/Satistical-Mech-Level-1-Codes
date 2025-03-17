import numpy as np
import matplotlib.pyplot as plt

# Constants
R = 8.314  # Gas constant (J/(mol K))

theta_E = 200  # Einstein temperature (K)
theta_D = 300  # Debye temperature (K)

# Temperature range
T = np.linspace(1, 500, 1000)

# Dulong-Petit Law
C_DP = np.full_like(T, 3 * R) 
'''full like creates an array as same shape as T and fill every elements with value 3*R
'''

# Einstein Model formula
E = theta_E / T
C_E = 3 * R * (E ** 2 * np.exp(E)) / (np.exp(E) - 1) ** 2

# Debye Model Formula
D = theta_D / T
C_D = 9 * R * (D ** 3) / (np.exp(D) - 1)

# Plot the results
plt.figure(figsize=(10,7))
plt.plot(T, C_DP, label='Dulong-Petit Law', linestyle='dashed')
plt.plot(T, C_E, label='Einstein Model', linestyle='dotted')
plt.plot(T, C_D, label='Debye Model', linestyle='solid')

plt.xlabel("Temperature (K)")
plt.ylabel("Specific Heat (J/mol K)")
plt.title("Specific Heat of Solids")
plt.legend()
plt.grid()
plt.show()


