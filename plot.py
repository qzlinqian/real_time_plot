# plot from random in rectangular coordinate

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# plt.close()
# clf() 清图
# cla() 清坐标轴
# close() # 关窗口
# plt.ion()
fig = plt.figure(figsize=(5, 5))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(0, 1), ax.set_xticks([])
ax.set_ylim(0, 1), ax.set_yticks([])
# unit = 2 * np.pi / 100
n = 100
pos = np.zeros(n, dtype=[('position', float, 2),
                         ('color', str, 1)])
pos['position'] = np.random.uniform(0, 1, (n, 2))
pos['color'] = 'r'
scat = ax.scatter(pos['position'][:, 0], pos['position'][:, 1], s=30, c=pos['color'])


def update(frame_number):
    # Get an index which we can use to re-spawn the oldest raindrop.
    current_index = frame_number % n

    pos['position'][current_index] = np.random.uniform(0, 1, 2)  # position update
    # color update
    if pos['position'][current_index, 1] < 0.5:
        pos['color'][current_index] = 'r'
    else:
        pos['color'][current_index] = 'b'

    # Update the scatter collection, with the new colors, sizes and positions.
    scat.set_offsets(pos['position'])
    scat.set_color(pos['color'])


animation = FuncAnimation(fig, update, interval=10)
plt.show()
