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

print((m[0]*g)/(2*I[0]*a[0]))
print((m[1]*g)/(2*I[1]*a[1]))

e1 = ((m[2]*g)/(48*I[2]*a[2]))
e2 = ((m[3]*g)/(48*I[3]*a[3]))

print(e1)
print(e2)

print((e1 + e2)/2)

print("--------------------")

l = [0.551, 0.6, 0.6]
sm = [0.1671, 0.5024, 0.1213]

print(sm[0]/(np.pi * (d[0]/2)**2) * l[0])

print(sm[1]/(l[1] * d[1]**2))

print(sm[2]/(l[2] * d[2]**2))