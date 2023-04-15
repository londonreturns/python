# this codes reads expression and calculates answer

def calculation(paraLine):
    currentLine = paraLine.strip()
    elements = currentLine.split(" ")
    operand1 = float(elements[0])
    operator = elements[1]
    operand2 = float(elements[2])
    if operator == "+":
        print(currentLine, "=",  operand1 + operand2)
    elif operator == "-":
        print(currentLine, "=", operand1 - operand2)
    elif operator == "*":
        print(currentLine, "=", operand1 * operand2)
    elif operator == "/":
        print(currentLine, "=", operand1 / operand2)

file1 = open("calculation.txt", "r")
for line in file1:
    calculation(line)
file1.close()