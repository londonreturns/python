try:
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("cannot divide by 0")
except ValueError:
    print("Entered value is wrong")