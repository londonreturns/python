try:
    num1 = 2
    num2 = 1
    result = num1 / num2
except ZeroDivisionError:
    print("cannot divide by 0")
else:
    print(result)