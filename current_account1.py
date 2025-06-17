from Account import Account  # Make sure Account.py exists and is correctly named

class CurrentAccount(Account):
    def __init__(self, account_number, holder_name, balance=0.0, overdraft_limit=5000):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        # Can go negative up to overdraft limit
        if amount > 0 and (self.balance - amount) >= -self.overdraft_limit:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance
