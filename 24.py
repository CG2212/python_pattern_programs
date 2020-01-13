#n=int(input("Enter the input:"))
n=7
for i in range(1,n+1):
	for j in range(1,i+1):
		if (j % 3) == 0:
			print(end=" @ ")
		elif (j % 2) == 0:
			print(end=" # ")
		else:
			print(end=" * ")
	print("")
