# this code calculates bmi and prints a message

# take input from user
weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))

# calculate bmi
bmi = weight / height ** 2

# check bmi and send message
if bmi < 18.5 :
    print(bmi, "is Underweight")
elif bmi < 25:
    print(bmi, "is Normal weight")
elif bmi < 30:
    print(bmi, "is Overweight")
else:
    print(bmi, "is Obese")