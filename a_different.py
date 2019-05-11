#a=input().split(' ')
f=open("file-two-number")
temp=[]
#print (list(f.read()))
for i in list(f.read()):
    print ("i=",i)

    if i=="":
        a = temp
        print ("a= ",a)
        temp.clear()
    if i=="\n":
        b = temp
        print ("b= ",b)
        temp.clear()
        print (abs(a-b))
    temp.append(i)

#print (abs(a[1]-a[0]))
#print (a.read())