# this code checks marks and grades them

# take input from user
num = int(input("number: "))
# check the marks and print out the grades in a loop
if num >= 90:
    # display output to user
    print("A")
elif num >= 80:
    print("B")
elif num >= 60:
    print("C")
else:
    print("Fail")
