def factorial(number):
    if number == 1:
        return 1
    return number * factorial(number - 1)

  
number = int(input('enter a positive number: '))
print(factorial(number))