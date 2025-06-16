from Account import Account
class CurrentAccount(Account):
    def __init__(self, account_number, holder_name, balance=0.0, overdraft_limit=5000):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        # Allowed to go negative up to overdraft_limit
        if amount > 0 and (self.balance - amount) >= -self.overdraft_limit:
            self.balance -= amount
            return True
