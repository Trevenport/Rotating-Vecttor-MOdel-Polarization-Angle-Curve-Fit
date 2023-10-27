import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd

# Load the data
data = pd.read_csv('1048-5832.csv')
#data = pd.read_csv('test.csv')

x = data['Pulse Longitude'] * np.pi / 180.0  # Convert to radians
y = data['PA'] * np.pi / 180.0  # Convert to radians

# Define the RVM function
def RVM(phi, alpha, beta, phi_0, psi_0):
    top = np.sin(alpha) * np.sin(phi - phi_0)
    bottom = np.sin(alpha + beta) * np.cos(alpha) - np.cos(alpha + beta) * np.sin(alpha) * np.cos(phi - phi_0)
    psi = np.arctan2(top, bottom)
    psi[psi > np.pi] -= np.pi
    psi[psi < np.pi] += np.pi
    return psi + psi_0

# Initial parameter guesses in radians
p0 = np.array([32, -44.95858, 4.02, -139.83]) * np.pi / 180.0
# Parameter bounds in radians
bbounds = np.array([[0, -180, -180, -180], [180, 180, 180, 180]]) * np.pi / 180.0

# Fit the curve
popt, pcov = curve_fit(RVM, x, y, p0, bounds=bbounds)
print(popt*180/np.pi)
yfit = RVM(x, *popt)

# Create a new figure and axis
fig, ax = plt.subplots()

# Plot the data and the fitted curve
ax.plot(x * 180 / np.pi, y * 180.0 / np.pi, label='Data', marker='o', linestyle='-', markersize=5,color='k')
ax.plot(x * 180 / np.pi, yfit * 180.0 / np.pi, label='fitted curve', linestyle='--',color='r')
#ax.plot(x * 180 / np.pi, yfit2 * 180.0 / np.pi, label='New', linestyle='--',color='y')

ax.set_xlabel('Pulse Longitude (degrees)')
ax.set_ylabel('PA (degrees)')
ax.set_title('RVM Fitting for J1048-5832')
ax.legend()
plt.tight_layout()
plt.show()
