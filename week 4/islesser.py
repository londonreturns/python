# this code prints the largest number

# take input from user
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

# check the greatest number and print in a loop
if num1 >= num2 and num1 >= num3:
    print(num1, "is the largest")
elif num2 >= num1 and num2 >= num3:
    print(num2, "is the largest")
else:
    print(num3, "is the largest")