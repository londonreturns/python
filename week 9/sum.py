total = 0
while True:
    try:
        new_element = input('enter a number (q for exit) ')
        if new_element == 'q':
            break
        num = int(new_element)
        total += num
    except ValueError:
        print('error')
print(total)