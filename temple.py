import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import math

# first set up the figure, the axis, and the plot element we want to animate
unit = 2 * math.pi / 100
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='polar')
line, = ax.plot([], [], lw=2)


def init():
    line.set_data([], [])
    return line


# animation function.  this is called sequentially
def animate(i):
    x = np.linspace(0, 2, 100)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line


anim = animation.FuncAnimation(fig, animate, init_func=init, frames=50, interval=10)
plt.show()
