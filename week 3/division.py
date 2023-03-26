# defining division function to two decimal places
def division(num1, num2):
    div = format(num1 / num2, ".2f")
    return div

# take inputs from user
number1 = float(input("Enter a number: "))
number2 = float(input("Enter a number: "))

# call division function and display output to user
print("The division answer is ", division(number1, number2))