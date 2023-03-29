# random number game

import random

tries = 1
a = random.randint(1, 20)
temp = ""

for tries in range(1, 6):
    ans = int(input("Enter a number: "))
    if a != ans:
        if ans > a:
            print("Not Correct, try again, Too high")
        else:
            print("Not Correct, try again, Too low")
        tries += 1
        temp += str(ans) + "\t"
    else:
        print("You won, in", tries, "tries")
        break


if tries == 6:
    print("You lost, the answer was", a)
    print("Your tries were", temp)