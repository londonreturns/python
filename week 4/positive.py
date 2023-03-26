# this code returns product of 2 positive number else sends error

# take input from user
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

# check
if num1 > 0 and num2 > 0:
    print(num1 * num2)
else:
    print("enter a positive number")