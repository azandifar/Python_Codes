#from threading import Thread
import os
from multiprocessing import Process

def factorial(n):
    s=1
    for x in range(2,n+1):
        s*=x
    print(s)

#t = Thread(target=dp_sth)
#t.start()
#t = Thread(target=dp_sth)
#t.start()

n = int(input())
for i in range(n):
    t = Thread(target=factorial,args=[int(input())])
    t.start()