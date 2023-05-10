sum = 0
while True:
    try:
        num = input('enter a integer: ')
        if num == 'q':
            break
        num = int(num)
        sum += num
    except ValueError:
        print('Invalid input')

print('sum is', sum)