# this code checks if a number is divisible by 2 and 3

# take input from user
num = int(input("Enter number: "))

# check if number is divisible by 2 and 3
if num % 2 == 0 and num % 3 == 0:
    # display output to user
    print("divisible by 2 and 3")
else:
    # display output to user
    print("not divisible by 2 and 3")