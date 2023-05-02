import random

random_number = random.randint(1, 10)
while True:
    try:
        choice = int(input('enter number '))
        if random_number == choice:
            print('you won')
            break
        else:
            print('try again')
    except ValueError:
        print('error')