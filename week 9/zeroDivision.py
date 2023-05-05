try:
    num1 = 2
    num2 = 0
    if num2 == 0:
        raise ZeroDivisionError
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("cannot divide by 0")