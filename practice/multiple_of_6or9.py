#Enter a number and show the message hello if the number is multiple of 6 or 9 otherwise show the message welcome
n = int(input('Enter a number: '))
if n%6 ==0 or n%9 ==0:
	print('Hello')
else:
	print('Welcome')
