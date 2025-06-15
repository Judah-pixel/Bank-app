class Account:
    def __init__(self, balance):
        self.balance = balance
        balance = 200000
        

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance = self.balance-amount
        else:
            print("Insufficient funds")

    def deposit(self, amount):
        self.balance += amount
            
