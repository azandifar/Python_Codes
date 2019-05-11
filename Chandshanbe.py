day=int(input("Please enter day: "))
month=int(input("Please enter month: "))
monthdays = day
if 1<month<=6:
    monthdays=(month-1)*31+day
elif 7<=month<=11:
    monthdays=186+(month-7)*30+day
elif month==12:
    monthdays=336+day
else:
    print("Please Enter valid month")

# if monthdays%7==1: chandshanbe = "4shanbe"
# if monthdays%7==2: chandshanbe = "5shanbe"
# if monthdays%7==3: chandshanbe = "Jome"
# if monthdays%7==4: chandshanbe = "shanbe"
# if monthdays%7==5: chandshanbe = "1shanbe"
# if monthdays%7==6: chandshanbe = "2shanbe"
# if monthdays%7==0: chandshanbe = "3shanbe"

chandshanbe = ['3shanbe','4shanbe','5shanbe','jome','shanbe','1shanbe','2shanbe']

#print("Rooze ",monthdays," sal yani: ",chandshanbe)
print(chandshanbe[monthdays%7])