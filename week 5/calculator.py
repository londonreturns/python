# this code repeatedly prompt the user for two numbers and an operation, loop until "q" to quit the program.

# initialising variables
sum = 0
difference = 0
product = 0
division = 0

while True:
    # take input from user
    numStr1 = input("Enter a number (or q to quit) ")
    if numStr1.lower() == "q":
        break
    numStr2 = input("Enter a number (or q to quit) ")
    if numStr2.lower() == "q":
        break
    operand = input("Enter an operand (or q to quit) ")
    if operand.lower() == "q":
        break
    num1 = int(numStr1)
    num2 = int(numStr2)
    if operand == "+":
        sum = num1 + num2
        print("Sum is", sum)
    elif operand == "-":
        difference = num1 - num2
        print("Difference is ", difference)
    elif operand == "*":
        product = num1 * num2
        print("Multiplication is", product)
    elif operand == "/":
        division = num1 / num2
        print("Division is", division)

