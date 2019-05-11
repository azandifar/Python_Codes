#lst = list( map( list, input().split( ' ' ) ) )
lst = input()
check = False
for i in range(len(lst)-1):
    if  (lst[i]+lst[i+1]=='ss'):
        check = True
if check:
    print('hiss')
else:
    print('no hiss')
