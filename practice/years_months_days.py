#WAP in python to enter total no. of days then show its fragments in following format- Year-Month-Weeks-Days. Take 1year=365 days and 1month=30days
d = int(input('Enter no. of days: '))
year = d//365
x = d%365
month = x//30
z = x%30
week = z//7
day = z%7
print(year,'years :',month,'months :',week,'weeks :',day,'days')
