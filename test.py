from math import pi
from dichotomy import search_min as d_search_min
from fibonachi import search_min as f_search_min
from parabola import search_min as p_search_min
from goldenratio import search_min as g_search_min
from brent import brent_min as b_search_min

print('Searching minimum for interval a = 3, b = 6, epsylon = 0.01')
print('----------------------------------------------------------')
a, b, e = 3, 6, 0.01
print('Dichotomy algorithm: ', d_search_min(a, b, 0.001, e))
print('Fibonachi algorithm: ', f_search_min(a, b, e))
print('Parabola algorithm: ', p_search_min(a, b, e))
print('Golden ratio algorithm: ', g_search_min(a, b, e))
print('Brent algorithm: ', b_search_min(a, b, e))
print('----------------------------------------------------------')

print('')

print('Searching minimum for interval a = 3pi, b = 4pi, epsylon = 0.01')
print('----------------------------------------------------------')
a, b, e = 3*pi, 4*pi, 0.01
print('Dichotomy algorithm: ', d_search_min(a, b, 0.001, e))
print('Fibonachi algorithm: ', f_search_min(a, b, e))
print('Parabola algorithm: ', p_search_min(a, b, e))
print('Golden ratio algorithm: ', g_search_min(a, b, e))
print('Brent algorithm: ', b_search_min(a, b, e))
print('----------------------------------------------------------')

print('')

print('Searching minimum for interval a = 16pi/3, b = 17pi/3, epsylon = 0.01')
print('----------------------------------------------------------')
a, b, e = 16*pi/3, 17*pi/3, 0.01
print('Dichotomy algorithm: ', d_search_min(a, b, 0.001, e))
print('Fibonachi algorithm: ', f_search_min(a, b, e))
print('Parabola algorithm: ', p_search_min(a, b, e))
print('Golden ratio algorithm: ', g_search_min(a, b, e))
print('Brent algorithm: ', b_search_min(a, b, e))
print('----------------------------------------------------------')