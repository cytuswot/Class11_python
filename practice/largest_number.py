#WAP to enter three numbers and find the largest number
x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
z = int(input('Enter third number: '))
if x>y and x>z:
	print(x,'is the largest number')
elif y>x and y>z:
	print(y,'is the largest number')
elif z>x and z>y:
	print(z,'is the largest number')
