# this code multiplies a series of integers input by the user, until a sentinel value of 0

# initiate variable
product = 1

# take input from user
num = int(input("Enter first numbers: "))

while num != 0:
    product = product * num
    num = int(input("Enter another number: "))

print("product is", product)
