### Dylan Bolger
### 11/5/2018
### CIS-120

def intro():
    print("Welcome to Michaels Catering Program.")
    print("This program converts cups to fluid ounces.")

def main():
    cups = input("Enter the number of cups: ")
    return cups

def conversion(cups):
    ounces = cups * 8
    print("There are " + str(ounces) + " fluid ounces in " + str(cups) + " cups.")

intro()
cups = int(main())
conversion(cups)
