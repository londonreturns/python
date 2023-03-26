#bmi calculator

#take input from user

weight = float(input("Enter user weight in kilograms: "))
height = float(input("Enter user height in meters: "))

#calculate bmi

bmi = weight / (height) ** 2

#display ouput

print("bmi is ", bmi)
