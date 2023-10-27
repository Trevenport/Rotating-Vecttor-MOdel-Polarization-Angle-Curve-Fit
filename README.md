# Rotating-Vecttor-MOdel-Polarization-Angle-Curve-Fit

Import necessary libraries:

numpy 
matplotlib for the plots.
scipy.optimize.curve_fit for fitting a model to data.
pandas for manipulating the data.

Load data using pandas. your columns are radians make sure you convert to radians.

Define the function with parameters of your choise

Initialize initial parameter guesses (p0) for the RVM model.

Define parameter bounds (bbounds) for the optimization. The bounds specify the minimum and maximum values for each parameter in radians.

Fit the RVM model to the data using scipy.optimize.curve_fit. This function optimizes the parameters to make the model fit the data as closely as possible and returns the optimized parameters in popt and the covariance of the parameters in pcov.

Print the optimized parameters (popt) converted from radians to degrees.

Generate fitted data (yfit) using the optimized parameters and the RVM function.

Create a plot.

Plot the original data points (x and y) and the fitted curve (x and yfit) on the same graph. The data points are shown as black circles ('Data') and the fitted curve as a red dashed line ('fitted curve'). Labels and legends are added to the plot for clarity.


