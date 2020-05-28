import numpy as np
from math import sqrt
from random import uniform
from scipy.optimize import fmin

k = 6
g = 3


def f(u):
    return u[0] ** 2 + (u[1] - g) ** 2 - 2 * k * g * u[0] + k


# повертає вектор частинних похідних для будь-якої кількості змінних
def dfdu(u):
    delta = 0.0001
    temp = [elem + delta for elem in u]
    res = []
    for i in range(len(u)):
        lst = u.copy()
        lst[i] = temp[i]
        res.append((f(lst) - f(u)) / delta)
    return res


def random_search(u0, h, e):
    M = 40
    counter = 0
    if h <= e:
        return f(u0)
    while True:
        E = np.array([uniform(-1, 1) for i in range(len(u0))])
        ui = u0 + h * E
        if f(ui) < f(u0):
            h *= 1.5
            temp = u0 + h * E
            if f(temp) < f(u0):
                return random_search(temp, h, e)
            else:
                counter += 1
                h /= 1.5
                if counter >= M:
                    h *= 0.5
        else:
            counter += 1
            if counter >= M:
                h *= 0.5


# градієнтний метод з поділом кроку навпіл
def gradient_descent(u0, h, e):
    while True:
        ui = u0 - h * np.array(dfdu(u0))
        if f(ui) >= f(u0):
            h *= 0.5
        else:
            break
    return f(ui) if sqrt(sum([elem ** 2 for elem in np.array(ui) - np.array(u0)])) <= e else gradient_descent(
        ui,
        h, e)


if __name__ == '__main__':
    h = 1.0
    e = 0.01
    u0 = [k * g + 2, g - 3]
    print("Gradient descent method: ", gradient_descent(u0, h, e))
    print("Random search method: ", random_search(u0, h, 0.0001))
    print(fmin(f, np.array(u0)))
