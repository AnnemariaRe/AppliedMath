from math import pi
import numpy as np
import matplotlib.pyplot as plt

from dichotomy import search_min as d_search_min
from fibonachi import search_min as f_search_min
from parabola import search_min as p_search_min
from goldenratio import search_min as g_search_min
from brent import brent_min as b_search_min

plt.figure(figsize=(6,7))

plt.subplot(2, 1, 1)
ax = plt.gca()
ax.set_xlabel('x')
ax.set_ylabel('y')

x , y = d_search_min(3, 6, 0.001, 0.01)
plt.scatter(x, y)
x , y = f_search_min(3, 6, 0.01)
plt.scatter(x, y)
x , y = p_search_min(3, 6, 0.01)
plt.scatter(x, y)
x , y = g_search_min(3, 6, 0.01)
plt.scatter(x, y)
x , y = b_search_min(3, 6, 0.01)
plt.scatter(x, y)

x , y = d_search_min(3*pi, 4*pi, 0.001, 0.01)
plt.scatter(x, y)
x , y = f_search_min(3*pi, 4*pi, 0.01)
plt.scatter(x, y)
x , y = p_search_min(3*pi, 4*pi, 0.01)
plt.scatter(x, y)
x , y = g_search_min(3, 6, 0.01)
plt.scatter(x, y)
x , y = b_search_min(3, 6, 0.01)
plt.scatter(x, y)

x , y = d_search_min(16*pi/3, 17*pi/3, 0.001, 0.01)
plt.scatter(x, y)
x , y = f_search_min(16*pi/3, 17*pi/3, 0.01)
plt.scatter(x, y)
x , y = p_search_min(16*pi/3, 17*pi/3, 0.01)
plt.scatter(x, y)
x , y = g_search_min(3, 6, 0.01)
plt.scatter(x, y)
x , y = b_search_min(3, 6, 0.01)
plt.scatter(x, y)

x = np.linspace(0, 20, 100)
y = np.sin(x) * x ** 2
plt.plot(x, y, label='f(x)')

plt.legend(loc="upper left", prop={'size': 7})
plt.xlim(3, 20)
plt.ylim(-300, 220)


plt.subplot(2, 1, 2)
ax = plt.gca()
ax.set_xlabel('accuracy')
ax.set_ylabel('iterations')

x = [0.01, 0.03, 0.08, 0.1]

a, y = d_search_min(3, 6, 0.001, 0.01)
a, y1 = d_search_min(3, 6, 0.001, 0.03)
a, y2 = d_search_min(3, 6, 0.001, 0.08)
a, y3 = d_search_min(3, 6, 0.001, 0.1)
data = [y, y1, y2, y3]
plt.plot(x, data, label='dichotomy')

a, y = f_search_min(3, 6, 0.01)
a, y1 = f_search_min(3, 6, 0.03)
a, y2 = f_search_min(3, 6, 0.08)
a, y3 = f_search_min(3, 6, 0.1)
data = [y, y1, y2, y3]
plt.plot(x, data, label='fibonachi')

a, y = p_search_min(3, 6, 0.01)
a, y1 = p_search_min(3, 6, 0.03)
a, y2 = p_search_min(3, 6, 0.08)
a, y3 = p_search_min(3, 6, 0.1)
data = [y, y1, y2, y3]
plt.plot(x, data, label='parabolic')

a, y = g_search_min(3, 6, 0.01)
a, y1 = g_search_min(3, 6, 0.03)
a, y2 = g_search_min(3, 6, 0.08)
a, y3 = g_search_min(3, 6, 0.1)
data = [y, y1, y2, y3]
plt.plot(x, data, label='golden ratio')

a, y = b_search_min(3, 6, 0.01)
a, y1 = b_search_min(3, 6, 0.03)
a, y2 = b_search_min(3, 6, 0.08)
a, y3 = b_search_min(3, 6, 0.1)
data = [y, y1, y2, y3]
plt.plot(x, data, label='brent')

plt.legend(loc="upper left", prop={'size': 6})
plt.ylim(5, 16)

plt.subplots_adjust(hspace=0.3, top=1)

plt.show()