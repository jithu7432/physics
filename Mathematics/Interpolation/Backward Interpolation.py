
"""Newton Gregory Forward Interpolation"""
from pandas import DataFrame


def ForwardDifference(Table):
    """Gives the forward difference of a list"""
    Difference = []
    i = 0
    l = len(Table)
    while i < l - 1:
        t = Table[i + 1] - Table[i]
        i = i + 1
        Difference.append(t)
    return Difference


def factorial(number):
    """Returns the factorial of an integer"""
    if number == 0:
        return 1
    return number * factorial(number - 1)


def coefficients(coefficient, num):
    """Gives the corresponding coefficients of the Newton Gregory Formula"""
    if num == 0:
        
        return 1
    temp = coefficient
    for i in range(1, num):
        temp = temp * (coefficient + i)
    return temp


# Reading X and Y values from the text file
X = list(map(float, open('data/xvalues.txt', 'r').read().split()))
Y = list(map(float, open('data/yvalues.txt', 'r').read().split()))

n = len(X)  # Number of terms
xvalue = 0.33  # The value at which f is to be calculated
DifferenceTable = [Y]  # Creating the Difference table as a nested list
h = X[1] - X[0]  # steps
u = (xvalue - X[-1]) / h  # u value

# Forming the difference table
for var in range(n):
    DifferenceTable.append(ForwardDifference(DifferenceTable[var]))

df = DataFrame(DifferenceTable).dropna(how='all').fillna("")  # For visualizing the Difference table

sum = 0

# Generating the sum
for k in range(0, n):
    t1 = coefficients(u, k) / factorial(k)
    t2 = DifferenceTable[k][-1]
    sum += (t1 * t2)

# Printing
print(df.transpose())
print("steps =", h, "& u =", u)
print("f(", xvalue, ") = ", sum, sep="")
