# this code calculates sum of digits of number

# take input from user
num = int(input("Enter a number: "))

# initiate variable
sum = 0

for i in range(1, len(str(num)) + 1):
    remainder = num % 10
    sum += remainder
    num = int(num/10)


print("Sum is", sum)