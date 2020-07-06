#ask for age 
#18-21 wristband
#21+ normal entry (you can drink)
#otherwise too young 

age = input("How old are you: ")
if age:
#you have to put int because u can't use op w/ string
	age = int(age)
	if age >= 18 and age < 21:
		print("You can enter, but you need a wristband")
	elif int(age) >= 21:
		print("You are good to go")
	else:
		print("You can't come in little one :(")
else:
	print("You have to enter your age!")