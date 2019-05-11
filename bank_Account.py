class accountInfo:
    def __init__(self):
        self.balance = 0
        self.transaction = []
    def deposit(self, value):
        self.balance += value
        self.transaction.append(['deposit',value])
    def withdraw(self,value):
        if self.balance - value >= 10000:
            self.balance-=value
            self.transaction.append(['withdraw',value])
    def __str__(self):
        return ('Balance: {}'.format(self.balance))
    def last_three(self):
        return self.transaction[-1 : -4 : -1]

a1 = accountInfo()
a1.deposit(100000)
a1.withdraw(5000)
a1.withdraw(7)
a1.withdraw(50)
print (a1)
print (*a1.last_three(),sep='\n')