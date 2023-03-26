# this code prompts user to input temperature in celcius

# prompt user for input
tempInC = float(input("Enter temperature in celcius: "))
# convert temperature celcius into farenheit
tempInF = (tempInC * 9 / 5) + 32
# display output to user
print("Temperature in Farenheit is ", tempInF)