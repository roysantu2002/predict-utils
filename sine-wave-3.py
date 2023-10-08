import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

plt.rcParams["figure.figsize"] = [10, 6]
plt.rcParams["figure.autolayout"] = True

fig, ax = plt.subplots()
ax.set_xlim(0, 2)
ax.set_ylim(0, 9)

line, = ax.plot([], [], lw=2)
age_markers = [0, 18, 36, 54, 72, 90]  # Age markers

def init():
    line.set_data([], [])
    return line,

def animate(i):
    x = np.linspace(0, 2, 1000)
    y = 4.5 * np.sin(2 * np.pi * (x - 0.01 * i)) + 4.5
    line.set_data(x, y)

    # Add age markers at the bottom
    for age in age_markers:
        ax.add_patch(plt.Circle((age / 100, 0), 0.03, color='green'))

    # Add age markers at the top
    for age in age_markers:
        ax.add_patch(plt.Circle((age / 100, 9), 0.03, color='green'))

    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)

# Set the x-axis labels
ax.set_xticks([age / 100 for age in age_markers])
ax.set_xticklabels([str(age) for age in age_markers])

plt.show()
