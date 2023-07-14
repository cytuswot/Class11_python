#Enter a symbol(+,-,*,/) then operate it accordingly and show the result
x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
print('Choices are: 1.Addition \n2.Subtraction \n3.Multiplication \n4.Division')
c = int(input('Enter your choice: '))
if c==1:
	print('Sum = ',x+y)
elif c==2:
	print('Subtraction = ',x-y)
elif c==3:
	print('Multiplication = ',x*y)
elif c==4:
	print('Division = ',x/y)
