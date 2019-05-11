def power(a,b):
    if b==1:
        return a
    return power(a,b//2)*power(a,b-b//2)

print(power(2,7))