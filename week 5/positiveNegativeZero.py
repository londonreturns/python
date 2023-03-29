# this code calculates number of positive, negative and zeros
# initiating variables
positiveCount = 0
negativeCount = 0
zeroCount = 0
wantToContinue = True

while True:
    if wantToContinue == True:
        # take input from user
        num = int(input("Enter a number: "))
        if num > 0:
            positiveCount += 1
        elif num < 0:
            negativeCount += 1
        else:
            zeroCount += 1
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
# display output to user
print("Number of Positives are: ", positiveCount)
print("Number of Negatives are: ", negativeCount)
print("Number of Zeros are: ", zeroCount)


