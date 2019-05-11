a=int(input("Enter number: "))
n=2
while n<=a:
    if n==a:
        print(a,"is prime")
    elif a%n==0:
        print (a,"is not prime")
        break
    n+=1

