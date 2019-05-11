class accountInfo:
    def __init__(self):
        self.balance = 0
        self.transaction = []

    def deposit(self, value):
        self.balance += value
        self.transaction.append( ['deposit', value] )

    def withdraw(self, value):
        if self.balance - value >= 10000:
            self.balance -= value
            self.transaction.append( ['withdraw', value] )

    def __str__(self):
        return 'Balance: {}'.format( self.balance )

    def last_three(self):
        return self.transaction[-1: -4: -1]


class shortTerm( accountInfo ):
    def __init__(self, r):
        super().__init__()
        self.rate = r

    def monthlyIncrease(self):
        self.balance = self.balance + (self.balance * self.rate) / 12
a1 = accountInfo()
b1 = shortTerm( 0.1 )
a1.deposit(500)
b1.deposit(500)
b1.monthlyIncrease()
print( 'a1= ', a1 )
print( 'b1= ', b1 )
# print (*a1.last_three(),sep='\n')
