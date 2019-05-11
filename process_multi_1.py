from multiprocessing import process

from time import time

def fact(b,e):
    s = b
    for x in range(b+1,e+1):
        s*=x
    return s
if __name__ == '__main__':
    n = int(input())
    p1 =process(target=fact, args=[1,n//2])
    p2 =process(target=fact, args=[n//2+1,n])
    p1.start()
    p2.start()
    p1.join()
    p2.join()