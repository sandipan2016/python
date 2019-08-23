def add():
	x=input('Enter the value of x:')
	y=input('Enter the value of y:')
	z=int(x)+int(y)
	print("The result of addition = ",z)
	
def sub():
	x=input('Enter the value of x:')
	y=input('Enter the value of y:')
	z=int(x)-int(y)
	print("The result of subtraction = ",z)
	
def mul():
	x=input('Enter the value of x:')
	y=input('Enter the value of y:')
	z=int(x)*int(y)
	print("The result of multiplication = ",z)
	
	
print('1.Add \n 2.Sub \n 3.Mul')
inp = input("Enter a mathematical operation:")
if(inp == 'Add'):
	add()
elif(inp == 'Sub'):
	sub()
else:
	mul()

	
