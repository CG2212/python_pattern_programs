#n=int(input("Enter the input:"))
n=7
for i in range(1,n+1):
	for j in range(1,n+1):
		if i == j:
			print(i,end=" ")
		else:
			print(end="0 ")
	print("")
