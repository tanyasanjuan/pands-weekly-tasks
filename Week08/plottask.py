# This program displays:
# - A histogram of a normal distribution of a 1000 values 
# with a mean of 5 and stadard deviation of 2,
# - and a plot of the function h(x) = x^3 in the range 0 to 10.
# on the one set of axes.
# Author: Tanya San Juan.

# Import numpy as np to use numpy 
# Import matplotlib.pyplot as plt to use matplotlib
import numpy as np
import matplotlib.pyplot as plt

# Normal distribution of 1000 values (1000 random numbers) with 
# a mean of 5 and standard deviation of 2 (mean=5, std=2).
# The mean is the average of the values in the array. The central value of the array.
# Source: https://en.wikipedia.org/wiki/Mean
# The standard deviation is the spread of the values in the array.
# Source: https://en.wikipedia.org/wiki/Standard_deviation
# np.random.normal is used to generate the values and store them in the variable normal_dist.
mean = 5
std_dev = 2
normal_dist = np.random.normal(mean, std_dev, 1000)

# Generate x values and corresponding y values for the function h(x) = x^3
# np.linspace is used to create an array and return spaced numbers over a specified interval.
# Source: https://www.geeksforgeeks.org/numpy-linspace/
# x = np.linspace(0, 10, 100) creates an array of 100 values from 0 to 10.
x = np.linspace(0, 10, 100)
# The function h(x) = x^3 is a cubic function. And it's calculated by raising x to the power of 3.
# calculates h(x) = x^3 for each value.
h_x = x**3


# The plot
# plt.figure(figsize) : Create a figure with a specified size (10 inches wide x 5 inches tall)
# Source: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html
plt.figure(figsize=(10, 5)) # Set the figure size to 10x5 inches.

# Plot the histogram with the data of normal distribution
# plt.hist is used to create a histogram of the normal distribution (normal_dist).
# The histogram can have parameters, like: (bins) of 30, and the color of the histogram: purple.
# Source: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
# The alpha parameter is used to set the transparency of the histogram. 0.5 is 50% transparent.
# Source: https://www.geeksforgeeks.org/change-the-line-opacity-in-matplotlib/
# label: Legend label for the histogram.
plt.hist(normal_dist, bins=30, color='purple', alpha= 0.5, label='Normal Distribution')
# plt.title is used to set the title of the plot.
plt.title ('Normal Distribution Histogram')


# The plot of the function h(x) = x^3
# plt.plot is used to plot the function h(x) = x^3. (It will draw a line.)
# The color of the line is aquamarine.
# The line width is set to 2. (the thickness of the line)
# The label is 'h(x) = x^3'
plt.plot(x, h_x, color='aquamarine', linewidth=2, label='h(x) = x^3')

# Labels and legend
# plt.title is used to set the title of the plot.
# plt.legend is used to show the legend of the plot.
# plt.xlabel is used to set the x-value label.
# plt.ylabel is used to set the y-value label.
plt.title('Normal Distribution Histogram and h(x) = x^3')
plt.xlabel('X-value')
plt.ylabel('Y-value')
plt.legend() # Show the legend with the labels of normal distribution and h(x) = x**3.
# plt.grid is used to show the grid on the plot.
# Source: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html
plt.grid(True) # Show the grid.
plt.show() # Show the plot.

# Safe the plot as a PNG file.
# plt.savefig is used to save the plot as a PNG file.
plt.savefig('normal_distribution_histogram_and_hx.png')