price = float
weight = input("What is the product's weight?\n")
if weight <= 2 :
	price = weight * 1.10
if weight > 2 and weight <= 6 :
	price = weight * 2.20
if weight > 6 and weight <= 10 :
	price = weight * 3.70
if weight > 10 :
	price = weight * 3.80
print("The shipping price is $" + str(price))