#JJ
from pandas import DataFrame


def f(v):
    return v ** 4 - 8 * v + 3


def df(u):
    return (f(u + h) - f(u)) / h


def ddf(z):
    return (df(z + h) - df(z)) / h


fl, dfl, xl, xll, ddfl = ([] for _ in range(5))
epsilon = 1e-5
h = 1e-5

x = float(input("Enter initial guess: "))
while True:
    xl.append(x), ddfl.append(ddf(x)), fl.append(f(x)), dfl.append(df(x))
    x = x - (f(x) / df(x)) - (f(x) * f(x) * ddf(x)) / (2 * (df(x) ** 3))
    xll.append(x)
    if abs(f(x)) <= epsilon:
        break
data = {"X": xl, "f(x)": fl, "f'(x)": dfl, "f''(x)": ddfl, "Xn": xll}
frame = DataFrame(data)
print(frame)
print("The root of the equation is:", x)
