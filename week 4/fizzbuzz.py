# fizzbuzz

# take input from user
num = int(input("Enter a number: "))

# initialise variable
temp = ""

# check if num is divisible by 3 and 5
if num % 3 == 0:
    # assign new characters to temp
    temp += "Fizz"
if num % 5 == 0:
    temp += "Buzz"

# display output to user
print(temp)
