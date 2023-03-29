# this code prints factorial of input from user

# take input from user
num = int(input("Enter a number: "))

# initiate variable
fact = 1

for i in range(2, num + 1):
    fact = fact * i

# display to user
print("Factorial is", fact)