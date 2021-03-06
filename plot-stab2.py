import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
    return content

def func(x, a, b):
    return a*x +b


werte = csv_read("csv/stab2_single-1191.5g.csv")
xdata = np.zeros(22)
ydata = np.zeros(22)
ignore = True
i=0

l=0.6

for values in werte:
    if(ignore):
        ignore = False
    else:
        xdata[i] = l*((float(values[0])*10**(-2))**2) - ((float(values[0])*10**(-2))**3)/3
        ydata[i] = float(values[2]) - float(values[1])
        
        i+=1

ydata = ydata * 10**(-3)

x_line = np.linspace(3, 48)*10**(-2)
x_line = l*(x_line**2) - (x_line**3)/3
plt.plot(xdata, ydata, 'bx', label="Messwerte")
popt1, pcov1 = curve_fit(func, xdata, ydata)
plt.plot(x_line, func(x_line, *popt1), "r-", label="Fit")
plt.xlabel(r"$g_\text{se}(x)$ / $\symup{m}^3$")
plt.ylabel(r"$D_\text{se}(x)$ / m")
print(popt1)
print(np.sqrt(np.diag(pcov1)))
plt.legend()
plt.tight_layout()
plt.savefig("build/stab2_single.pdf")