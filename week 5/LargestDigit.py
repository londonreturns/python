# this code finds the largest digit in a number entered by the user using a loop

# take input from user
num = int(input("Enter number: "))

# initiate values
maxDigit = 0

for i in range(0, len(str(num))):
    newDigit = num % 10
    if newDigit > maxDigit:
        maxDigit = newDigit
    num = int(num / 10)


# display output to user
print("Max number is", maxDigit)