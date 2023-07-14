"""
Calculate the sum of first and last digit of a number
"""

# 1. Take a number input
number = input("Enter a number: ")

# 2. extract first and last digits
first_digit = int(number[0])
last_digit = int(number[-1])

# 3. add them

sum = first_digit + last_digit
print("sum =", sum)




