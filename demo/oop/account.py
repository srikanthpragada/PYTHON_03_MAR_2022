class Account:
    # Static attribute or class attribute
    minbal = 10000
    @staticmethod      # Decorator
    def getminbal():
        return Account.minbal

    # constructor
    def __init__(self, acno, ahname, balance=0):
        # Object Attributes
        self.acno = acno
        self.ahname = ahname
        # private attribute
        self.__balance = balance

    # Methods
    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance < amount:
            raise ValueError("Insufficient Balance")

        self.__balance -= amount

    def getbalance(self):
        return self.__balance

    def show(self):
        print("Acno     : ", self.acno)
        print("Ahname   : ", self.ahname)
        print("Balance  : ", self.__balance)


print(Account.getminbal())

a1 = Account(1, "Scott")  # Create an object/instance
a1.deposit(10000)
a1.deposit(20000)
a1.withdraw(100000)
print(a1.__dict__)
# print(a1._Account__balance)

# a1.show()

a2 = Account(2, "Mark", 50000)
# a2.show()
