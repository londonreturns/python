# this function calculates average
def avg(n1, n2, n3, n4, n5):
    total = 5 * 100
    return ((n1 + n2 + n3 + n4 + n5) / total) * 100


# take input from user
num1 = int(input("Enter marks: "))
num2 = int(input("Enter marks: "))
num3 = int(input("Enter marks: "))
num4 = int(input("Enter marks: "))
num5 = int(input("Enter marks: "))
# calling avg function and displaying output
print("Your percentage is :", format(avg(num1, num2, num3, num4, num5), ".2f"), "%")