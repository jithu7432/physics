#JithinJohnson
from pandas import DataFrame


def f(g):
    return g ** 3 - 8 * g + 3


a = float(input("Enter a: "))
b = float(input("Enter b: "))
epsilon = 1e-5
listA,listB,listX,listF = ([] for _ in range(4))
if f(a) * f(b) > 0:
    raise ValueError
while True:
    x = (a + b) / 2
    listX.append(x),listA.append(a),listB.append(b),listF.append(f(x))
    if f(x) * f(a) < 0:
        b = x
    else:
        a = x
    if f(a) <= epsilon and f(b) <= epsilon:
        break
df = DataFrame({'a': listA, 'b': listB, 'x': listX, 'f(x)': listF})
print(df)
