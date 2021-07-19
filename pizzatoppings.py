toppingCount = 0
while True:
	## in the variable, topping, I'm using raw_input to receieve the string value rather than Python
	## attempting to interpret it. Using a regular input method, I'm required to include quotations while inputting.
	topping = raw_input("Enter a topping to add to your pizza (Type \"Done\" when complete): ")
	if topping != "Done" :
		print("You have added " + topping + " to your pizza.")
		toppingCount += 1
		if toppingCount > 1:
			print("You have a total of " + str(toppingCount) + " toppings on your pizza.\n")
		else:
			print("You have " + str(toppingCount) + " topping on your pizza.\n")
	else:

		print("\nThe cost of the pizza before toppings: $5.99")
		toppingPrice = float(toppingCount) * 0.15
		subtotal = toppingPrice + 5.99
		salestax = subtotal * 0.04
		total = subtotal + salestax
		print("The cost of additional toppings: $" + str(toppingPrice) + "0")
		print("The subtotal of the pizza: $" + str(subtotal))
		print("The cost of sales tax (At 4%) is $" + str(salestax))
		print("The total pizza cost is $" + str(total))
		break
