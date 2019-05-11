input_string1 = input("Enter List1: ")
input_string2 = input("Enter List2: ")
list1 = input_string1.split(" ")
list2 = input_string2.split(" ")
print("list1= ",list1)
print("list2= ",list2)
ejtema_list=[]
eshterak_list=[]
yektaie_list1=list1
yektaie_list2=list2
for i in list1:
    print ("i= ",i)
    for j in list2:
        print("j=",j)
        if i == j:
            eshterak_list.append(i)
            # yektaie_list1.remove(i)
            # yektaie_list2.remove(i)

print("Eshterak= ", eshterak_list)
# print("Yektai list1", yektaie_list1)
# print("Yektai list2", yektaie_list2)
# ejtema_list = yektaie_list1+eshterak_list+yektaie_list2
# print("Ejtema= ",ejtema_list)
