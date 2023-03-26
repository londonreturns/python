# this program reads two numbers and prints sum is even or odd

# initialise sum
sum = 0

# take input from user
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

# calculate sum of the numbers
sum = num1 + num2

# check if sum is even or odd
if sum % 2 == 0:
    print("Sum is", sum, "which is even")
else:
    print("Sum is", sum, "which is odd")
    