# print fibonnaci numbers


x=0
y=1
ctr=0
z=0

print(x)
print(y)

while ctr<7:
	z=x+y
	x=y
	y=z
	print(z)
	ctr=ctr+1


