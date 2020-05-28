from random import uniform
from math import sqrt
from scipy.optimize import fmin

k = 6
g = 3


def f(x):
    return x ** 2 + 2 * k * g * x + k


def dichotomy_method(a, b, e=0.01):
    xm = (a + b) / 2
    x1 = a + (b - a) / 4
    x2 = b - (b - a) / 4
    if b - a <= e:
        return f(xm)
    if f(xm) >= f(x2):
        return dichotomy_method(xm, b, e)
    elif f(xm) >= f(x1):
        return dichotomy_method(a, xm, e)
    else:
        return dichotomy_method(x1, x2, e)


def monte_carlo_method(a, b, N):
    min = f(uniform(a, b))
    for i in range(N - 1):
        temp = f(uniform(a, b))
        min = temp if temp < min else min
    return min


if __name__ == '__main__':
    a = -k * g - 2
    b = k * g + 1
    e = 0.01
    N = 100
    print('Function: x^2 + {}*x + {}'.format(2*k*g, k))
    print('Interval: [{}, {}]'.format(a, b))
    print('Min(Monte-Carlo method): {}  (e = {})'.format(monte_carlo_method(a, b, N), 1/(sqrt(N))))
    print('Min(Dichotomy method): {}  (e = {})'.format(dichotomy_method(a, b), e))
    print('Actual value:')
    print(fmin(f, 0))