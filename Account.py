class Account:
    def __init__(self, balance):
        self.balance = balance
        balance = 200000
        

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance = self.balance-amount
            return True
        else:
            print("Insufficient funds")
            return False

    def deposit(self, amount):
        #to deposit the amount to the account
        if amount > 0:
            self.balance += amount
            return True
        return False
            
