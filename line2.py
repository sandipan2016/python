fhand = open('D:\\python\\line.txt')
inp = fhand.read()
i=0
cnt=0
ctr=0
cnt=len(inp)
print(cnt)
while(i<cnt):
		if(inp[i]=='.'):
				ctr=ctr+1
				i=i+1
				continue
		else:
				print(inp[i])
				i=i+1
print(ctr)
		

