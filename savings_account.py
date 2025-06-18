from Account import Account

class SavingsAccount(Account):
    def __init__(self, account_number="SA-001", holder_name="John Doe", balance=200000):
        super().__init__(account_number, holder_name, balance)
        self.limit = 10000

    def withdraw(self, amount):
        if amount <= self.limit:
            return super().withdraw(amount)
        else:
            return False



