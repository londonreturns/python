# this code will sum until user enters 0

# take input from user
num = int(input("Enter number"))

# defining addition
addition = 0

# loop
while num != 0:
    addition = addition + num
    num = int(input("Enter number"))

# display output to user
print("Sum is", addition)
