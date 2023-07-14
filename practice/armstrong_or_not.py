#WAP to enter a no. and check whether it is Armstrong or not
n = int(input('Enter a number: '))
s,k = 0,n
while n>0:
	x = n%10
	n = n//10
	s = s+(x**3)
if k==s:
	print(k,'is armstong')
else:
	print(k,'is armstong')
