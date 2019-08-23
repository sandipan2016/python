def chop(arr):
	j=0
	while(j<5):
		if(j==0):
				arr[j]=" "
				j=j+1
		elif(j==4):
				arr[j]=" "
				j=j+1
		else:
				j=j+1
	return arr
	
	

	
	
	
	
arr=["0","0","0","0","0"]
i=0
while(i<5):
	arr[i] = input("Enter element in list\n")
	i=i+1

arr=chop(arr)
print(arr)









