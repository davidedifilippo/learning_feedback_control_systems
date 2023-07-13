import control
import matplotlib.pyplot as plt
import numpy as np

# Funzione di trasferimento ad anello aperto
# F(s) = 1/((s+3)^2*(s-1))

num = [1]
den = [1, 5, 3, -9]

F = control.tf(num, den)
print("F=", F)

# poli e zeri della F(s)
plt.figure(1)
pz = control.pzmap(F, plot=True, grid=True)
print(pz)


# Funzione di trasferimento ad anello chiuso
W = control.feedback(F, 1)
print("W=", W)

#Trova le radici della W(s) al variare del guadagno K del ramo diretto
plt.figure(2)
control.root_locus(F, initial_gain=0, print_gain=True)

plt.show()
