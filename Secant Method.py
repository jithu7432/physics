#JJ
from pandas import DataFrame


def f(u):
    return u ** 3 - 8 * u + 3


x = float(input("x: "))
b = float(input("b: "))
epsilon = 1e-5
xl, bl, fxl, fbl, xnl, fxnl = ([] for _ in range(6))
while True:
    xl.append(x), bl.append(b), fxl.append(f(x)), fbl.append(f(b))
    x = x - (f(x) / (f(b) - f(x))) * (b - x)
    xnl.append(x), fxnl.append(f(x))

    if abs(f(x)) <= epsilon:
        break
print("The root of the equation is:", x)
data = {"x": xl, "b": bl, "f(x)": fxl, "f(b)": fbl, "xn": xnl, "f(xn)": fxnl}
print(DataFrame(data))
