# prove that a number is prime


div=2
flg=0
inp1=0

inp=input("Enter the number to prove prime\n")

inp1 = int(inp)


while div<inp1:
		if inp1%div!=0:
			div=div+1
			continue
		else:
			flg=1
			break
if flg==0:
	print("input is prime")
else:
	print("input is non-prime")
	
	



