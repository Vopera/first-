class Bank(object):
	print('Welcome to Damola\' bank')
	def __init__(self, balance=0.0):
		self.balance = balance
	
	def display_balance(self):
		print(f'your balance is {self.balance}')
		
	def make_deposit(self):
		amount = float(input('Input the amount of 			money you want to deposit >>'))
		self.balance += amount
		print(f'After deposit, your balance is {self.				balance}')
		
	def withdraw(self):
		amount = int(input('how much do you want 		to withraw >>>'))
		if amount > self.balance:
			print('Insufficient balance')
		else:
			self.balance = (self.balance - amount)
			print(f' Withdraw succesful, you have {self.			balance}')
		
#	def get_detail(self):
#		print(f' {sef.display_balance}, {sef.							make_deposit}, {sef.withdraw}')
			
stra = int(input('enter your balance >>'))
sef = Bank(stra)


#print(sef.get_detail())

print(sef.display_balance())

print(sef.make_deposit())

print(sef.withdraw())

