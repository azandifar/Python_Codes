lst=['a','a','b','b','b']
dic={}
for i in lst:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(dic)