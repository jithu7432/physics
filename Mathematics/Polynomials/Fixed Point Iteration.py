#JithinJohnson
from pandas import DataFrame


f = lambda v: v ** 3 - 8 * v + 3


phi = lambda u : (3 + u ** 3) / 8


dphi = lambda z: (phi(z + h) - phi(z)) / h


h = 1e-5

print("Choose x : phi'(x) is < 1")

x = float(input("x: "))

if dphi(x) > 1:
    print("phi'(x) > 1")
    raise ValueError

epsilon = 1e-5

xl, phixl, fxl = ([] for _ in range(3))

while True:
    xl.append(x), phixl.append(phi(x)),fxl.append(f(x))
    x = phi(x)
    if abs(f(x)) <= epsilon:
        break

data = DataFrame({"x": xl, "phi(x)": phixl, "f(x)": fxl})
print("The root is:", x)
print(data)
