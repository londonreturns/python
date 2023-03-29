# this code calculates price of electricity

# take input from user
units = int(input("Enter units: "))

if units <= 100:
    charge = 0
elif units <= 200:
    charge = units * 5
else:
    charge = 100 * 5 + (units - 200) * 10

print("charge is", charge)
