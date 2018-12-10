import numpy as np
from uncertainties import ufloat
from uncertainties.umath import *

I = np.zeros(4)
d = np.array([10, 10, 10.4, 10.4]) * (10**(-3))

I[0] = (np.pi * d[0]**4)/64
I[1] = (d[1]**4)/12
I[2] = (d[2]**4)/12
I[3] = (d[3]**4)/12

print(I)

m = [0.418, 1.1915, 2.3618, 2.3618]
g = 9.81
a = [ufloat(63.9, 0.5) * (10**(-3)), ufloat(66.2, 0.5) * (10**(-3)), ufloat(6.137, 0.09) * (10**(-3)), ufloat(6.7, 0.2) * (10**(-3))]
#rund, einseitig
#eckig, einseitig
#rechts, beidseitig
#links, beidseitg

for i in range(4):
    print((m[i]*g)/(2*I[i]*a[i]))