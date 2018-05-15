import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
import math

plt.close()
# clf() 清图
# cla() 清坐标轴
# close() # 关窗口
plt.ion()
fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(1, 1, 1, projection='polar')
unit = 2 * math.pi / 100
degree = list()
length = list()

while 1:
    a = int(input())
    b = int(input())
    degree.append(a)
    length.append(b)
    plt.polar(a * unit, b)
    plt.pause(0.001)
