import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [10, 4]
plt.rcParams["figure.autolayout"] = True

fig, ax = plt.subplots()
ax.set_xlim(0, 1.08)
ax.set_ylim(-1.5, 1.5)

x = np.linspace(0, 1.08, 1000)
y = np.zeros_like(x)
ax.plot(x, y, color='black', lw=2)

bottom_age_markers = [0, 18, 36, 54, 72, 90, 108]
top_age_markers = [9, 27, 45, 63, 81, 99]

# Add events at the ages of 10, 15, and 19
event_ages = [10, 15, 19]
event_colors = ['green', 'red', 'red']  # Green for positive, Red for negative

marker_radius = 0.015
number_offset = 0.03  # Offset for the numbers outside the markers

for age in bottom_age_markers:
    circle = plt.Circle((age / 108, -0.1), marker_radius, color='green', fill=True)
    ax.add_patch(circle)
    ax.annotate(str(age), (age / 108, -0.1 - number_offset), ha='center', va='center', color='black')

# Adjust the position of the number for age 9
x_event = 9 / 108
y_event = 0.1 + 0.5 * np.sin(2 * np.pi * x_event * 10)
marker = plt.Line2D([x_event], [y_event], marker='*', markersize=8, color='green')
ax.add_line(marker)
ax.annotate(str(0), (x_event, y_event + number_offset), ha='center', va='center', color='black')

for age in top_age_markers[0:]:  # Exclude age 9 from the loop
    circle = plt.Circle((age / 108, 0.1), marker_radius, color='green', fill=True)
    ax.add_patch(circle)
    ax.annotate(str(age), (age / 108, 0.1 + number_offset), ha='center', va='center', color='black')

# Create a sine wave connecting all markers
x_wave = np.linspace(0, 108 / 108, 1000)  # Full x range
y_wave = 0.5 * np.sin(2 * np.pi * x_wave * 10)

# Shift the sine wave up to the top ruler
y_wave += 0.1

# Plot the sine wave
ax.plot(x_wave, y_wave, color='blue', lw=2)

# Add the marker for age 9 at the first peak
x_event = 9 / 108
y_event = 0.1 + 0.5 * np.sin(2 * np.pi * x_event * 10)
marker = plt.Line2D([x_event], [y_event], marker='*', markersize=8, color='green')
ax.add_line(marker)
ax.annotate(str(9), (x_event, y_event + number_offset), ha='center', va='center', color='black')

# Add events as markers on the sine wave with star markers
for age, color in zip(event_ages, event_colors):
    x_event = age / 108
    y_event = 0.1 + 0.5 * np.sin(2 * np.pi * x_event * 10)
    marker = plt.Line2D([x_event], [y_event], marker='*', markersize=8, color=color)
    ax.add_line(marker)
    ax.annotate(str(age), (x_event, y_event + number_offset), ha='center', va='center', color='black')

ax.set_xticks([])
ax.set_yticks([])
ax.set_xticklabels([])
ax.set_yticklabels([])

plt.show()
