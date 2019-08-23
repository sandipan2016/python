inp = input("Enter a number\n")
i=1
j=0
inp=int(inp)
while(i<=inp):
	s=inp%i
	i=i+1
	if s !=0:
		continue
	else:
		j=j+1
	if i>inp:
		break
if j==2:
	print("prime")
else:
	print("not prime")

	
	