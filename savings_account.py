from Account import Account

class SavingsAccount(Account):
	def __init__(self, balance):
		super().__init__(balance)
		self.limit = 10000

	def withdraw(self, amount):
		if amount <= self.limit:
			super().withdraw(amount)
		elif amount > self.limit:
			print("Amount exceeds limit")
	

		
