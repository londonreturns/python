# this code displays output to corresponding credits

# take input from user
credit = int(input("Enter number of credits: "))

# check the credits
if credit >= 90:
    print("Senior Status")
elif credit >= 60:
    print("Junior Status")
elif credit >= 30:
    print("Sophomore Status")
else:
    print("Freshman Status")