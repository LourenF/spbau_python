import random
import time
import sys
import multiprocessing

N = 10000000

def hypotenuse(s):
    x = random.random()
    y = random.random()
    R = 0
    h = (x**2 + y**2)**0.5
    if h <= 1:
        R += 1
    return R

def coordinates(pool):
    l = pool.map(hypotenuse, [0]*N)
    return l

if __name__ == '__main__':
    pool = multiprocessing.Pool()
    t0 = time.time()
    N_kr = sum(coordinates(pool))
    Pi_ = 4*(N_kr/N)
    print("Число Пи:", Pi_)
    print("Потраченное время:", time.time() - t0)
else:
    print(__name__)