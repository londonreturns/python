# this code prints fibonacci of n terms

# take input from user
num = int(input("How many fibonacci numbers? "))

# initiate variables
a = 0
b = 1
temp = 0

for i in range(0, num):
    # display output to user
    print(a)
    temp = a
    a = a + b
    b = temp