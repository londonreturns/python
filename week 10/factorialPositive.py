def factorial(number):
    if number == 1:
        return 1
    return number * factorial(number - 1)

try:
    num = int(input("Enter a number: "))
    if num < 0:
        raise ValueError
    print(factorial(num))
except ValueError:
    print("please enter positive number")
