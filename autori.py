lst = list(input())
lst2=[]
for i in lst:
    if i.isupper():
        lst2.append(i)
for j in lst2:
    print(j, end="")