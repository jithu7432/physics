#JJ
from pandas import DataFrame


def f(v):
    return v ** 3 - 8 * v + 3


def phi(u):
    return (3 + u ** 3) / 8


def dphi(z):
    return (phi(z + h) - phi(z)) / h


h = 1e-5
print("Choose x : phi'(x) is < 1")
x = float(input("x: "))
if dphi(x) > 1:
    print("phi'(x) > 1")
    raise ValueError
epsilon = 1e-5
xl, phixl, fxl = ([] for _ in range(3))
while True:
    xl.append(x), phixl.append(phi(x))
    x = phi(x)
    fxl.append(f(x))
    if abs(f(x)) <= epsilon:
        break
data = DataFrame({"x": xl, "phi(x)": phixl, "f(x)": fxl})
print("The root is:", x)
print(data)
