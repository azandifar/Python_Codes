#import sys
#for line in sys.stdin:
#    xyn = line.strip("\n").split("")
#    x = int(xyn[0])
#    y = int(xyn[1])
#    n = int(xyn[2])
lst = list(map(int,input().split(' ')))
x,y,n=lst[0],lst[1],lst[2]
if 1<=x<y<n<=100:
    for i in range(1,n+1):
        if i%x==0 and i%y==0:
            print('FizzBuzz')
            continue
        elif i%x==0:
            print ('Fizz')
            continue
        elif i%y==0:
            print ('Buzz')
            continue
        else :
            print(i)
else:
    print ('Please enter correct numbers')