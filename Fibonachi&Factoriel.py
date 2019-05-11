n=int(input("Please enter n: "))
a=0
b=1
for i in range(0,n-1):
    c=a+b
    a=b
    b=c
print("Fibomachi number for" ,n, "omin is ",c)
f=1
for i in range(1,n+1):
    f=f*i
print("factoriel " ,n,"! is:",f)