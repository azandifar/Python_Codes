class Employee:
    def __init__(self,n,s):
        self.name = n
        self.salary = s
    def __str__(self):
        return 'Name: {}, Salary: {}'.format(self.name,self.salary)

class Programmer(Employee): # Programmer child of Employee
    def __init__(self,n,s,l):
        super().__init__ (n,s)
        self.language = l
    def __str__(self):
        return super().__str__()+' Language: {}'.format (self.language)

e1 = Employee ('Amir', 10 ** 6)
print(e1)

p1 = Programmer('Hooman',10**7,'Python')
print(p1)