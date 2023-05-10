def gcd(num1, num2):
    if num2 == 0:
        return num1
    return gcd(num2, num1 % num2)

def input_number():
    while True:
        try:
            num = int(input('Enter a number: '))
            if num < 1:
                raise ValueError
            return num
        except ValueError:
            print('enter a positive number')

num1 = input_number()
num2 = input_number()

print('greatest common denominator is', gcd(num1, num2))