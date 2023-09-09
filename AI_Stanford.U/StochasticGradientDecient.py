import numpy as np

true_w = np.array([1, 2, 3, 4, 5])
d = len(true_w)
points = []
for i in range(500000):
    x = np.random.randn(d)
    y = true_w @ x + np.random.randn()
    points.append((x, y))

def F(w):
    return sum((w @ x - y)**2 for x, y in points) / len(points)

def dF(w):
    return sum(2 * (w @ x - y) * x for x, y in points) / len(points)

def SF(w, i):
    X, y = points[i]
    return (w @ x - y)**2

def sdF(w, i):
    X, y = points[i]
    return 2 * (w @ x - y) * x

def gradient_descent(F, dF, d):
    w = np.zeros(d)
    eta = 0.01
    for t in range(1000):
        value = F(w)
        gradient = dF(w)
        w = w - eta * gradient
        print(f'iteration {t}: w = {w}, F(w) = {value}')

def stochastic_gradient_descent(sF, sdF, d, n):
    w = np.zeros(d)
    eta = 1
    num_updates = 0
    for t in range(1000):
        for i in range(n):
            value = SF(w, i)
            gradient = sdF(w, i)
            num_updates += 1
            eta = 1.0 / num_updates
            w = w - eta * gradient
        print(f'iteration {t}: w = {w}, F(w) = {value}')

gradient_descent(F, dF, d)
stochastic_gradient_descent(SF, sdF, d, 10)
