import numpy as np

true_w = np.array([1, 2, 3, 4, 5])
d = len(true_w)
points = []
for i in range(700000):
    X = np.random.randn(d)
    y = true_w @ X + np.random.randn()
    points.append((X, y))

def F(w):
    return sum((w @ X - y)**2 for X, y in points) / len(points)

def dF(w):
    return sum(2 * (w @ X - y) * X for X, y in points) / len(points)

def gradient_descent(F, dF, d):
    w = np.zeros(d)
    eta = 0.01
    for t in range(1000):
        value = F(w)
        gradient = dF(w)
        w = w - eta * gradient
        print(f'iteration {t}: w = {w}, F(w) = {value}')

gradient_descent(F, dF, d)