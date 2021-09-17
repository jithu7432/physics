import numpy as np
import matplotlib.pyplot as plt


l = 3
m = []
for i in range(-l, l+1):
    m += [i]

L = np.sqrt(l * (l+1))

c = [ml/L for ml in m]

t = np.arccos(c)
s = np.sin(t)

x = np.linspace(0, 1, 10)

plt.figure(figsize=(6, 6))

for i in range(len(c)):
    plt.plot(x*s[i], x*c[i],label=f"{t[i] * 180/np.pi :04.2f}")

plt.xlim(+0, 2)
plt.ylim(-1, 1)
plt.legend()
plt.show()
