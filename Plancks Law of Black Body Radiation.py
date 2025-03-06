import numpy as np
import matplotlib.pyplot as plt
from scipy import constants as sc

h = sc.Planck
c = sc.speed_of_light
k = sc.Boltzmann
pi = sc.pi
l = np.linspace(0.1, 50, 6000)  
l0 = l * 1e-06  

def planck_frm(l0, t):
    x = 8 * pi * h * c
    y = (h * c) / (l0 * k * t)
    z = np.exp(y) - 1
    f = (x / (l0**5)) / z  
    return f


R_Ht = (8* pi *k *1100)/l0**4 #Rayleigh's law at High temperature  
R_Lt = (8*pi*k*200)/l0**4 #Rayleigh's law at Low temperature 

plotplnck1 = planck_frm(l0, 600)
plotplnck2 = planck_frm(l0, 800)
plotplnck3 = planck_frm(l0, 1000)
plotplnck4 = planck_frm(l0, 1200)
plt.figure(figsize=(10,7))
plt.plot(l0, plotplnck1,label='600k')
plt.plot(l0, plotplnck2,label='800k')
plt.plot(l0, plotplnck3,label='1000k')
plt.plot(l0, plotplnck4,label='1200k')
plt.legend(loc="best" ,prop={'size':12})
plt.xlabel(r"$\lambda$ ")  
plt.ylabel(r"U($\lambda $,T )")
plt.title("Planck Law of Radiation")
plt.ylim(0,500)
plt.xlim(0,0.00002) #Arbitrary Value

plt.show()
plt.figure(figsize=(10,7))
plt.plot(l0, (planck_frm(l0,200)),label='Planck Law')
plt.plot(l0, R_Lt , "--" , label="Rayleigh-Jeans Law")
plt.ylim(0,0.5)
plt.xlim(0,0.00003) #Arbitrary Value
plt.show()

plt.figure(figsize=(10,7))
plt.plot(l0, (planck_frm(l0,1200)),label='Planck Law')
plt.plot(l0, R_Lt , "--" , label="Rayleigh-Jeans Law")
plt.ylim(0,450) #Arbitrary Value
plt.show()

