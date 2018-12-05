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


werte = csv_read("csv/stab1_dual-2361.8g.csv")
xdata = np.zeros(11)
ydata = np.zeros(11)
ignore = True
i=0

l=0.58

for values in werte:
    if(i >= 11):
        break
    if(ignore):
        ignore = False
    else:
        xdata[i] = 3*l**2*((float(values[0])*10**(-2))) - ((float(values[0])*10**(-2))**3)*4
        ydata[i] = float(values[2]) - float(values[1])
        
        i+=1
ydata = ydata * 10**(-3)

x_line = np.linspace(3, 26)*10**(-2)
x_line = 3*l**2*(x_line) - (x_line**3)*4

plt.plot(xdata, ydata, 'bx', label="Messwerte")
popt1, pcov1 = curve_fit(func, xdata, ydata)
plt.plot(x_line, func(x_line, *popt1), "r-", label="Fit")
plt.xlabel(r"$g_\text{dr}(x)$ / $\symup{m}^3$")
plt.ylabel(r"$D_\text{dr}(x)$ / m")
print(popt1)
print(np.sqrt(np.diag(pcov1)))
plt.legend()
plt.tight_layout()
plt.savefig("build/stab1_1_dual.pdf")
