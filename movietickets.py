while True:
	age = input("How old are you?\n")
	if age == "quit" or "Quit" or "exit" or "Exit" :
		break
	age = int(age)

if age < 3:
	print("Your ticket is free!")
elif age < 13:
	print("Your ticket costs $10")
else:
	print("Your ticket costs $15")