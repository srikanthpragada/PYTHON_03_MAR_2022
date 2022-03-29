class Account:
    # constructor
    def __init__(self, acno, ahname, balance=0):
        # Attributes
        self.acno = acno
        self.ahname = ahname
        self.balance = balance

    # Methods
    def deposit(self, amount):
        self.balance += amount

    def getbalance(self):
        return self.balance

    def show(self):
        print("Acno     : ", self.acno)
        print("Ahname   : ", self.ahname)
        print("Balance  : ", self.balance)


a1 = Account(1, "Scott")  # Create an object/instance
a1.deposit(10000)
a1.deposit(20000)
print(a1.getbalance())

a1.show()

a2 = Account(2, "Mark", 50000)
a2.show()
