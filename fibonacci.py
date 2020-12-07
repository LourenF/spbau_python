class Fib:
    '''По объектам этого класса можно итерироваться и получать числа Фибоначчи'''

    def __init__(self, a):
        self.max = a
        self.fib1 = 1
        self.fib2 = 1
        self.i = 1

    def __next__(self):
        fib = self.fib1
        j = self.i
        if j > self.max:
            raise StopIteration
        self.i += 1
        self.fib1, self.fib2 = self.fib2, self.fib1 + self.fib2
        return fib

    def __iter__(self):
        return self


for n in Fib(10):
    print(n, end = ' ')
