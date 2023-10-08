import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

plt.rcParams["figure.figsize"] = [10, 6]
plt.rcParams["figure.autolayout"] = True

fig, ax = plt.subplots()
ax.set_xlim(0, 2)
ax.set_ylim(0, 9)

line, = ax.plot([], [], lw=2)
bottom_age_markers = [0, 18, 36, 54, 72, 90, 108]  # Age markers at the x-axis (bottom)
top_age_markers = [9, 27, 45, 63, 81]  # Age markers at the top of the y-axis

def init():
    line.set_data([], [])
    return line,

def animate(i):
    x = np.linspace(0, 2, 1000)
    y = 4.5 * np.sin(2 * np.pi * (x - 0.01 * i)) + 4.5
    line.set_data(x, y)

    # Add age markers at the x-axis (bottom) with green circular markers
    for age in bottom_age_markers:
        ax.add_patch(plt.Circle((age / 100, 0), 0.03, color='green'))

    # Add age markers at the top of the y-axis with red circular markers
    for age in top_age_markers:
        ax.add_patch(plt.Circle((0, age), 0.03, color='red'))

    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)

# Set the x-axis labels without blank markers
ax.set_xticks([age / 100 for age in bottom_age_markers])
ax.set_xticklabels([str(age) for age in bottom_age_markers])

plt.show()
