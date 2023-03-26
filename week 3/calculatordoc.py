# calculator program
# this function performs addition
def addition(n1, n2):
    """This function takes two input and
    adds them"""
    return n1 + n2
# this function performs subtraction
def subtraction(n1, n2):
    """This function takes two input and
        subtracts them"""
    return n1 - n2
# this function performs multiplication
def multiplication(n1, n2):
    """This function takes two input and
        multiplies them"""
    return n1 * n2
# this function performs division
def division(n1, n2):
    """This function takes two input and
        divides them"""
    return n1 / n2
# this function performs addition
def modulus(n1, n2):
    """This function takes two input and
        mods the first number by second"""
    return n1 % n2
# this function performs addition
def exponent(n1, n2):
    """This function takes two input and
        takes the power of them"""
    return n1 ** n2

# take input from user
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))

# calling functions and their docstrings
help(addition)
print("Addition is", addition(num1, num2))
help(subtraction)
print("Subtraction is", subtraction(num1, num2))
help(multiplication)
print("Multiplication is", multiplication(num1, num2))
help(division)
print("Division is", division(num1, num2))
help(modulus)
print("Modulus is", modulus(num1, num2))
help(exponent)
print("Exponent is", exponent(num1, num2))