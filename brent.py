from math import sin, sqrt

# like uuuuuu uuuuuuu
import null as null

ratio = (sqrt(5) - 1) / 2


def f(x):
    return sin(x) * x ** 2


def parabolic_approximation(x1, x2, x3, f1, f2, f3):
    if (2 * ((x2 - x1) * (f2 - f3) - (x2 - x3) * (f2 - f1))) == 0:
        return null
    else:
        u = x2 - ((x2 - x1) ** 2 * (f2 - f3) - (x2 - x3) ** 2 * (f2 - f1)) / (
                2 * ((x2 - x1) * (f2 - f3) - (x2 - x3) * (f2 - f1)))
        return u


def brent_min(a, b, e):
    x = w = v = a + ratio * (b - a)
    dp = dc = b - a
    fx = fw = fv = f(x)
    while b - a > e:
        g = dp / 2
        dp = dc
        u = parabolic_approximation(x, w, v, fx, fw, fv)
        if (u == null) or ((a <= u <= b) != 1) or (abs(u - x) > g):
            if x < (a + b) / 2:
                u = x + ratio * (b - x)
                dp = b - x
            else:
                u = x - ratio * (x - a)
                dp = x - a

        dc = abs(u - x)
        if f(u) > f(x):
            if u < x:
                a = u
            else:
                b = u
            if f(u) <= f(w) or w == x:
                v = w
                w = u
            elif f(u) <= f(v) or v == x or v == w:
                v = u
        else:
            if u < x:
                b = x
            else:
                a = x
            x = w
            w = x
            x = u

    return x


print(brent_min(-3, 0, 0.001))
