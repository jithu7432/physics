from pandas import DataFrame

A = [1, -6, 11, -6]
B = []
Roots = []

iterations = 9 # Watch out for overflow errors

for n in range(iterations):
    for i in range(0, len(A)):
        if i == 0:
            B.append(A[0])
        elif i == len(A) - 1:
            B.append(A[-1] * A[-1])
        else:
            B.append(A[i] * A[i] - 2 * A[i - 1] * A[i + 1])
    roots = []
    for jj in range(3):
        roots.append(((B[jj + 1]) / (B[jj])) ** (2 ** (-(n + 1))))
    Roots.append(roots)
    A = B
    B = []

df = DataFrame(Roots)
df.columns = ["X1", "X2 ", "X3"]
print(df)
