# Dylan Bolger
### CIS - 120
# Exam 3
run = True
selecting = True
totalCredits = 0
registeredClassCount = 0
classOptions = [
    [1, "CIS-170", "Java", "(3)"],
    [2, "CIS-131", "WebDev II", "(3)"],
    [3, "CIS-250", "Database", "(3)"],
    [4, "MTH-110", "College Algebra", "(4)"],  # 4 creds
    [5, "ACC-210", "Accounting", "(3)"]
]
selectedClasses = []

def introduction():
    print("Welcome to Class Registration.\n")
    studentName = input("What is your name?: ")
    print("Hello " + studentName + "!")
    print("\nHere are your class options:")
    for classes in classOptions:
        for c in classes:
            print(c, "", end=" ")
        print()  # print a new line after each value is printed.


def selectingClasses():
    global registeredClassCount
    global totalCredits
    global classOptions
    global selectedClasses
    selectedClass = input("\nChoose a class to register in: ")
    if selectedClass == "1":
        selectedClasses.append(classOptions[0])
        totalCredits += 3
        registeredClassCount +=1
    elif selectedClass == "2":
        selectedClasses.append(classOptions[1])
        totalCredits += 3
        registeredClassCount +=1
    elif selectedClass == "3":
        selectedClasses.append(classOptions[2])
        totalCredits += 3
        registeredClassCount +=1
    elif selectedClass == "4":
        selectedClasses.append(classOptions[3])
        totalCredits += 4
        registeredClassCount +=1
    elif selectedClass == "5":
        selectedClasses.append(classOptions[4])
        totalCredits += 3
        registeredClassCount +=1


def main():
    global registeredClassCount
    global selecting
    global selectedClasses
    global run
    global totalCredits
    while run:
        introduction()
        while selecting:
            selectingClasses()
            continueSelecting = input("Would you like to add more classes?: ")
            if continueSelecting == "n" or continueSelecting == "N":
                print("\nYou are registered in the following classes:")
                for classes in selectedClasses:
                    classString = classes[1] + " : " + classes[3] + " credits"
                    print(str(classString))
                print()
                print("You are registered in", registeredClassCount, "classes.")
                print("Total Credits:", totalCredits, "\n")
                print("Thank you for registering!")
                selecting = False
                run = False


if __name__ == '__main__':
    main()
