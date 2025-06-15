from Account import Account
class Current_Account(Account):
    def __init__(self, balance):
        super().__init__(balance)

CurrentAccount = Current_Account(200000)
CurrentAccount.deposit(1000)
CurrentAccount.withdraw(500)


