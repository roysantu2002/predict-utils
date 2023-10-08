import numpy as np
import matplotlib.pyplot as plt

# Generate a range of x values from 0 to 18 intervals
x = np.linspace(0, 18, 1000)

# Calculate the corresponding sine values for the x values
y = np.sin(x)

# Create the figure and axis objects
fig, ax = plt.subplots()

# Plot the sine wave
ax.plot(x, y, label='Sine Wave')

# Add a vertical line at the 9th interval (x=9)
center_x = 9
ax.axvline(x=center_x, color='red', linestyle='--', label='Center (x=9)')

# Set axis labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Sine Wave with Center Line')

# Add a legend
ax.legend()

# Show the plot
plt.grid()
plt.show()
