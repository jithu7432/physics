import math

class Interpolate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.n = len(x)

    def forward(self):
        array = [self.x, self.y]
        for _ in range(4):
            temp = []
            y = array[-1]
            for i in range(len(y) - 1):
                temp += [y[i + 1] - y[i]]
            array += [temp]
        return array
    
    def backward(self):
        array = [self.x, self.y]
        for _ in range(4):
            temp = []
            y = array[-1]
            for i in range(len(y) - 1):
                temp += [y[i] - y[i+1]]
            array += [temp]
        return array

    def newtons(self,xval,table):
        self.xval = xval
        self.step = self.x[1] - self.x[0]
        self.uval = (self.xval - self.x[0]) / self.step
        def coefficients(coefficient, num):
            if num == 0:
                return 1
            temp = coefficient
            for i in range(1, num):
                temp = temp * (coefficient - i)
            return temp
        self.table = table[1:]        
        sums = 0
        for k in range(0, self.n):
            t1 = coefficients(self.uval, k) / math.factorial(k)
            t2 = self.table[k][0]
            sums += (t1 * t2)
        return sums


x = [1, 2, 3, 4, 5]  # Set of X values
y = [1, 4, 9, 16, 25]  # Set of Y values


data = Interpolate(x,y)

forward  = data.forward()
backward = data.backward()

print(data.newtons(table=forward,xval=12))