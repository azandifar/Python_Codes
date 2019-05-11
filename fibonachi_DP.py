from time import time
def fibDP(n):
    fibLst=[1,1]
    for i in range (2,n):
        fibtemp=fibLst[i-1]+fibLst[i-2]
        fibLst.append(fibtemp)
    return fibLst[-1]
n=int(input())
t1=int(time())
print(fibDP(n))
t2=int(time())
print (t2-t1)

