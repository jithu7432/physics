#JihtinJohnson
from pandas import DataFrame


def f(x):
    return x ** 3 - 8 * x + 3


def df(x):
    return (f(x + h) - f(x)) / h


fl, dfl, xl, xll = ([] for _ in range(4))
epsilon = 1e-10
h = 1e-10
x = float(input("Enter initial guess: "))
while True:
    xl.append(x), fl.append(f(x)), dfl.append(df(x))
    x = x - f(x) / df(x)
    xll.append(x)
    if abs(f(x)) <= epsilon:
        break
data = {"X": xl, "f(x)": fl, "f'(x)": dfl, "Xn": xll}
frame = DataFrame(data)
print(frame)
print("The root of the equation is:", x)
