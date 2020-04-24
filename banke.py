import random
print('Welcome to Damola\'s bank')
print('insert your card')


pin = int(input('input your pin number >><'))

while pin != 1996:
		print('wrong pin,')
		pin=int(input ('your pin number >><'))
		print()
print('Welcome Jumoke')
print('Choose your option')
print(' (1) balance \n (2) withdraw \n (3) recharge \n (4)Transfer ')
opti = int(input('option'))
print()

if opti == 1:
	balance = random.randint(4000,90000)
	print('your balance is', balance)

elif opti ==2:
	print('How much do you want to withdraw')
	print( '500 \n 1000 \n 2000 \n 5000 \n other')
	wit = int(input('option'))
	balance = random.randint(20000,567777)
	if (wit == 500 or wit == 1000 or wit ==2000 or 		wit ==5000) < balance:
		print()
		print('You have succesfully withdraw', wit)
		print()
	else:
		
		if wit == 5:
			other=int(input('input the withdraw amount'))
			if other < balance:
				print('yu have succesfully withdraw')
				
elif 

			
			



