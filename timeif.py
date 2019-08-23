time =0
time = int(input("Enter time in 24hr format\n"))

if time>0 and time<=12:
		print("Good Morning",time)
elif time>=13 and time<=16:
		print("{0} is Good Afternoon".format(time))
elif time>=17 and time<=20:
		print("{0} is Good Evening".format(time))
elif time>=21 and time<=24:
		print("{0} is Good Night".format(time))
else:
		print("Wrong input")
		