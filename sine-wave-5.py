import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [10, 4]
plt.rcParams["figure.autolayout"] = True

fig, ax = plt.subplots()
ax.set_xlim(0, 1.08)
ax.set_ylim(-1.5, 1.5)

# Define the x-axis markers at 9-year intervals
x_markers = np.arange(0, 109, 9)
y_marker = 0.1  # Y-coordinate for the top ruler markers

# Add markers and labels to the x-axis
for age in x_markers:
    ax.plot(age / 108, y_marker, 'o', markersize=8, color='green')
    ax.annotate(str(age), (age / 108, y_marker + 0.05), ha='center', va='center', color='black')

# Create a sine wave connecting all markers
x_wave = np.arange(0, 109, 1) / 108  # Markers at 9-year intervals
y_wave = 0.5 * np.sin(2 * np.pi * x_wave * 10) + 0.1  # Shifted to align with the top markers

# Plot the sine wave
ax.plot(x_wave, y_wave, color='blue', lw=2)

ax.set_xticks([])
ax.set_yticks([])
ax.set_xticklabels([])
ax.set_yticklabels([])

plt.show()
