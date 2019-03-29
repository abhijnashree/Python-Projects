class AccountManager:
	def __init__(self,account_name,account_no,balance,pin):
		self.account_name=account_name
		self.account_no=account_no
		self.balance=balance
		self.pin=pin
		self.transactions=[]
		

	def deposit(self,amount):
		if amount>10000:
			print
		self.balance+=amount
		print("your current balance is",self.balance)

	def withdrawal(self,amount):
		if self.balance<amount:
			print("insufficient balance")
		else:
			self.balance-=amount
		print("your current balance is",self.balnce)	


	def show_balance(self):	
		print("your current balance is",self.balnce)	

