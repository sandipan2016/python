fhand=open('D:\\python\\file11.txt')
for line in fhand:
	line=line.rstrip()
	#print(line)
	if line.find('@gmail')!=-1:
		continue
	print(line)
	
	
