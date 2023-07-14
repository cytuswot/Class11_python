#Enter 3 sides of a triangle and find its area
a = int(input('Enter first side: '))
b = int(input('Enter second side: '))
c = int(input('Enter third side: '))
s = (a+b+c)/2
a_t = (s*(s-a)*(s-b)*(s-c))**0.5
print('Area of triangle = ',round(a_t,2))
