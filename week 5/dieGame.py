# this code is random die game

from random import randint

# initiate value
isGame = True

while isGame:
    while True:
        totalDieSum = randint(1, 6) + randint(1, 6)
        # take input from user
        guessSum = int(input("Enter the sum of two dies: "))
        if guessSum == totalDieSum:
            print("Correct")
        else:
            print("Not Correct")
        again = input("Press q to quit ")
        if again.lower() == "q":
            isGame = False
            break
