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
ignore = 12
i=0

l=0.58

for values in werte:
    if(i >= 11):
        break
    if(ignore > 0):
        ignore -= 1
    else:
        xdata[i] = 4 * (float(values[0])*10**(-2))**3 - 12 * l * (float(values[0])*10**(-2))**2 + 9*l**2*(float(values[0])*10**(-2)) - l**3
        ydata[i] = float(values[2]) - float(values[1])
        
        i+=1

ydata = ydata * 10**(-3)

crrct = [xdata[0],xdata[2],xdata[3],xdata[4],xdata[6],xdata[7],xdata[8],xdata[9], xdata[10]]
crrcty = [ydata[0],ydata[2],ydata[3],ydata[4],ydata[6],ydata[7],ydata[8],ydata[9],ydata[10]]

x_line = np.linspace(29, 52)*10**(-2)
x_line = (-12)*l*(x_line**2) + (x_line**3)*4 + 9*(l**2)*x_line - l**3

plt.plot(crrct, crrcty, 'bx', label="Messwerte")
plt.plot([xdata[1], xdata[5]], [ydata[1], ydata[5]], 'bo', label="Nicht betrachtete Messwerte")
popt1, pcov1 = curve_fit(func, crrct, crrcty)
plt.plot(x_line, func(x_line, *popt1), "r-", label="Fit")
plt.xlabel(r"$g_\text{dl}(x)$ / $\symup{m}^3$")
plt.ylabel(r"$D_\text{dl}(x)$ / m")
print(popt1)
print(np.sqrt(np.diag(pcov1)))
plt.legend()
plt.tight_layout()
plt.savefig("build/stab1_2_dual.pdf")
