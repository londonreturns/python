all_num = []
while True:
    try:
        num = input("Enter a number or q to end: ")
        if num.lower() == 'q':
            break
        if not num.isdigit():
            raise ValueError
        all_num.append(int(num))
        
    except ZeroDivisionError:
        print('No values entered')
    except ValueError:
        print('Invalid input')

try:
    sum = 0
    count = 0
    for number in all_num:
        sum += number
        count += 1
    print('average is', sum / count)
except ZeroDivisionError:
    print('no inputs')
