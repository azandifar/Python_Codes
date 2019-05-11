from time import time
def func(n):
    if (n==1):
        return(1)
    elif(n==2):
        return(1)
    return(func(n-1)+func(n-2))
n=int(input())
t1=int(time())
print(func(n))
t2=int(time())
print (t2-t1)

