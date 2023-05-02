#근사 적분값

import math

def v(t):
    return math.exp(t) - 1

def trapezoidal(f, a, b, n):
    h = (b - a) / n
    f_sum = 0
    for i in range(1, n, 1):
        x = a + i * h
        f_sum += f(x)
    return h * (0.5 * f(a) + f_sum + 0.5 * f(b))

approximation = trapezoidal(v, 0, 3, 100)
print(approximation)

# t가 1일 떄 0.7

