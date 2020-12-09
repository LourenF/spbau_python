import itertools

class Fib:
    '''По объектам этого класса можно итерироваться и получать числа Фибоначчи'''

    def __init__(self):
        self.fib1 = 1
        self.fib2 = 1

    def __next__(self):
        fib = self.fib1
        self.fib1, self.fib2 = self.fib2, self.fib1 + self.fib2
        return fib

    def __iter__(self):
        return self

for i in itertools.islice(Fib(), 10):
    print(i)
