import numpy as np
import matplotlib.pyplot as plt

# Define the years from 0 to 90 with 9-year intervals
years = np.arange(0, 91, 9)

# Create an array to represent the amplitudes corresponding to the years
amplitudes = [0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0]  # Adjusted to match the length of years

# Create the figure and axis objects
fig, ax = plt.subplots()

# Plot the amplitudes as a step function
ax.step(years, amplitudes, where='mid', label='Age Step')

# Set the x-axis ticks to show the years
ax.set_xticks(years)

# Set the y-axis limits to be 0 to 9
ax.set_ylim(0, 9)

# Set axis labels and title
ax.set_xlabel('Years')
ax.set_ylabel('Amplitude')
ax.set_title('Step Function for Age Intervals')

# Show the plot
plt.grid()
plt.show()
