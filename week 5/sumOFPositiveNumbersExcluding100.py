# this code Sums a series of (positive) integers entered by the user, excluding all numbers that are Greater than 100.

# initiate variables
sum = 0
wantToContinue = True

while True:
    if wantToContinue == True:
        # take input from user
        num = int(input("Enter a number: "))
        if 0 < num < 100:
            sum += num
    else:
        break
    while wantToContinue == True:
        # prompt the user if they want to continue
        again = input("Do you want to continue? Press yes or no ")
        if again.lower() == "n" or again.lower() == "no":
            wantToContinue = False
            break
        elif again.lower() == "y" or again.lower() == "yes":
            break

print("Sum is", sum)