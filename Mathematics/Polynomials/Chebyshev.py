#JJ
from pandas import DataFrame


f = lambda v: v ** 4 - 8 * v + 3


df = lambda u:(f(u + h) - f(u)) / h


ddf = lambda z: (df(z + h) - df(z)) / h


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
