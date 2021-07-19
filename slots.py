##Dylan Bolger
##CIS-120
##10/22/18
##Instruction said to end the game when cash = 0, I ended the game when the player can no longer bet (cash < 25)
import random
print("Welcome to the slots game!")
cash = 100
play = 1
fruits = ("Cherries",
          "Oranges",
          "Plums",
          "Bells",
          "Melons",
          "Bars")
while play == 1:
    if cash < 25:
        print("You can not afford to play this game")
        break
    bet = input("What is your bet? ($25 minimum bet) $")
    bet = int(bet)
    while bet > cash:
        print("You bet a value that is higher than you have in cash.")
        bet = input("What is your bet? ($25 minimum bet) $")
        bet = int(bet)
    bet = int(bet)
    while bet < 25:
        print("Error, you bet below the minimum of $25. Try again.")
        bet = input("What is your bet? ($25 minimum bet) $")
        bet = int(bet)
    cash = cash - bet
    print("You bet $" + str(bet) + ", leaving you with $" + str(cash) + " remaining.")
    fruitOne = random.choice(fruits)
    fruitTwo = random.choice(fruits)
    fruitThree = random.choice(fruits)
    print("You pull the handle:")
    print("| " + fruitOne + " | " + fruitTwo + " | " + fruitThree + " |")
    if fruitOne == fruitTwo:
        if fruitTwo == fruitThree:
            winning = 75
            cash += winning
            print("You matched three! You won $75")
            print("You have $" + str(cash) + " in cash.")
        else:
            winning = 25
            cash += winning
            print("You matched two! You won $25")
            print("You have $" + str(cash) + " in cash.")
    elif fruitTwo == fruitThree:
        winning = 25
        cash += winning
        print("You matched two! You won $25")
        print("You have $" + str(cash) + " in cash.")
    elif fruitOne == fruitThree:
        winning = 25
        cash += winning
        print("You matched two! You won $25")
        print("You have $" + str(cash) + " in cash.")
    else:
        print("You did not match any.")
        print("You have $" + str(cash) + " in cash.")
    playAgain = input("Would you like to play again?")
    if playAgain == "no":
        play = 0
        print("Thanks for playing! You have $" + str(cash) + " remaining.")
    
