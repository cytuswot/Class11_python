#WAP in python to add two time zones and show the final time values
h1 = int(input('Enter first time zone hours: '))  
h2 = int(input('Enter second time zone hours: '))
m1 = int(input('Enter first time zone minutes: '))
m2 = int(input('Enter second time zone minutes: '))
s1 = int(input('Enter first time zone seconds: '))
s2 = int(input('Enter second time zone seconds: ')) 
sec = (s1+s2)%60
mins = (m1+m2)%60
hr = h1+h2+(m1+m2)//60
print(hr,'hrs.:',mins,'mins:',sec,'sec')
