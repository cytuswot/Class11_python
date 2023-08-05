n = 14
for i in range(1,4):
	for j in range(1,n):
		if i<4 and j<4:
			print("+",end="")
		else:
			print("-",end="")
	n = n-3
	print()

