from asyncio.windows_events import NULL
from math import sin, sqrt
import math

ratio = (sqrt(5) - 1) / 2


def f(x):
    return sin(x) * x ** 2


def parabolic_approximation(x1, x2, x3, f1, f2, f3):
    if (2 * ((x2 - x1) * (f2 - f3) - (x2 - x3) * (f2 - f1))) == 0:
        return NULL
    else:
        u = x2 - ((x2 - x1) ** 2 * (f2 - f3) - (x2 - x3) ** 2 * (f2 - f1)) / (
                2 * ((x2 - x1) * (f2 - f3) - (x2 - x3) * (f2 - f1)))
        return u


def brent_min(a, b, e):
    x = w = v = a + ratio * (b - a)
    dp = dc = b - a
    fx = fw = fv = f(x)
    iter = 0
    list = []

    while b - a > e:
        iter += 1
        g = dp / 2
        dp = dc
        u = parabolic_approximation(x, w, v, fx, fw, fv)
        if (u == NULL) or ((a <= u <= b) != 1) or (abs(u - x) > g):
            if x < (a + b) / 2:
                u = x + ratio * (b - x)
                dp = b - x
            else:
                u = x - ratio * (x - a)
                dp = x - a

        fu = f(u)
        dc = abs(u - x)
        if fu > fx:
            if u >= x:
                b = u
            else:
                a = u
            if fu < fw or w == x:
                v = w
                w = u
                fv = fw
                fw = fu
            elif fu < fv or v == x or v == w:
                v = u
                fv = fu
        else:
            if u > x:
                a = x
            else:
                b = x
            v = w
            w = x
            x = u
            fv = fw
            fw = fx
            fx = fu
        list.append((b, a))

    return x, iter, list
