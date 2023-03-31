# this code is random die game

from random import randint

# initiate value
isGame = True
count = 0
numberOfWins = 0

while isGame:
    while True:
        totalDieSum = randint(1, 6) + randint(1, 6)
        # take input from user
        guessSum = int(input("Enter the sum of two dies: "))
        if guessSum == totalDieSum:
            print("Correct")
            numberOfWins += 1
        else:
            print("Not Correct")
        count += 1
        again = input("Press q to quit ")
        if again.lower() == "q":
            isGame = False
            break

print("Number of times played", count)
print("Win percentage", round( numberOfWins / count, 2), "%")