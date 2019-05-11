def nfuctor(n):
    r=1
    for i in range (1,n+1):
        r*=i
    return (r)

def aval(a):
    while n <= a:
        if n == a:
            print(a, "is prime")
            return 1
        elif a % n == 0:
            print(a, "is not prime")
            return 0
        n += 1
