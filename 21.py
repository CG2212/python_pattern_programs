#n=int(input("Enter the input:"))
n=7
for i in range(1,n+1):
	for j in range(1,i+1):
		if (j % 2) == 0:
			print(end=" 0 ")
		else:
			print(end=" 1 ")
	print("")
