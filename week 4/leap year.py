# this code checks if a year is leap year

# take input from user
year = int(input("Enter year: "))

# checks for leap year
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("leap year")
else:
    print("not leap year")


