#WAP to calculate SI and CI
P = int(input('Enter Principle Amount: '))
R = int(input('Enter Rate of Interest: '))
T = int(input('Enter Time Period: '))
SI = (P*R*T)/100
CI = P*(1+R/100)**T
print('Simple Interest = ',round(SI,2))
print('Compound Interest = ',round(CI,2))
