# this code finds the least digit in a number entered by the user using a loop

# take input from user
num = int(input("Enter number: "))

# initiate values
leastDigit = 9

for i in range(0, len(str(num))):
    newDigit = num % 10
    if newDigit < leastDigit:
        leastDigit = newDigit
    num = int(num / 10)


# display output to user
print("Least number is", leastDigit)