# this code print lowest number

# take input from user
num1 = int(input("Enter a num: "))
num2 = int(input("Enter a num: "))

# check the lower number
if num1 == num2:
    print("Equal numbers")
elif num1 > num2:
    print(num2, "is lower")
else:
    print(num1, "is lower")