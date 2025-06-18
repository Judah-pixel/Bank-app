class Account:
    def __init__(self, account_number, holder_name, balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            return False
        self.balance -= amount
        return True

    def deposit(self, amount):
        if amount <= 0:
            return False
        self.balance += amount
        return True

    def get_balance(self):
        return self.balance