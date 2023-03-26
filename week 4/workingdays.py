# this code will calculate percentage of working days

# take input from user
working_days = int(input("Number of working days: "))
absent_days = int(input("Number of absent days: "))

# calculate percentage
percent = working_days / (working_days + absent_days) * 100

# check if working percentage is greater than 80
if percent >= 80:
    print("eligible")
else:
    print("ineliglible")