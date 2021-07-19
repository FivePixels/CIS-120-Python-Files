guestCount = input("How many guests will be attending the cookout?\n")
hotdogCount = input("How many hot dogs will be offered to each guest?\n")

expectedCount = guestCount * hotdogCount

bunPackageCount = guestCount * hotdogCount // 8
hdPackageCount = guestCount * hotdogCount // 10

if guestCount * hotdogCount % 8 == 0 and guestCount * hotdogCount % 10 == 0:
    print(str(bunPackageCount) + " packages of hot dog buns are needed.") 
    print(str(hdPackageCount) + " packages of hot dogs are needed.")
    print("The number of hot dog buns that will be left over is 0")
    print("The number of hot dogs that will be left over is 0")
elif guestCount * hotdogCount % 8 == 0 and guestCount * hotdogCount % 10 != 0:
    print(str(bunPackageCount) + " packages of hot dog buns are needed.") 
    print(str(hdPackageCount + 1)+ " packages of hot dogs required.")
    print("The number of hot dog buns that will be left over is " + str(expectedCount % 8))
    print("The number of hot dogs that will be left over is " + str(((hdPackageCount + 1) * 10 - guestCount * hotdogCount)))
elif guestCount * hotdogCount % 8 != 0 and guestCount * hotdogCount % 10 == 0:
    print(str(bunPackageCount + 1) + " packages of hot dog buns required.")
    print(hdPackageCount + " packages of hot dogs required.")
    print("The number of hot dog buns that will be left over is " + str(((bunPackageCount + 1) * 8 - guestCount * hotdogCount)))
    print("The number of hot dogs that will be left over is " + str(expectedCount % 10))
else:
    print(str(bunPackageCount + 1) + " packages of hot dog buns required.")
    print(str(hdPackageCount + 1) + " packages of hot dogs required.")
    print("The number of hot dog buns that will be left over is " + str(((bunPackageCount + 1) * 8 - guestCount * hotdogCount)))
    print("The number of hot dogs that will be left over is " + str(((hdPackageCount + 1) * 10 - guestCount * hotdogCount)))