# this code reverses string

# take input from user
strng = input("Enter a string: ")

# initiate variable
reverseString = ""

for i in range(0, len(strng)):
    reverseString = strng[i] + reverseString

# display output to user
print(reverseString)