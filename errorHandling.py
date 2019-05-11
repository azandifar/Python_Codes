try:
    a = int (input())
    b = int (input())
    print (a/b)
#except:
#    print('Enter again')
except ZeroDivisionError as x:
    print (x)
except ValueError as x:
    print (x)
except 
    print( 'Please input again' )