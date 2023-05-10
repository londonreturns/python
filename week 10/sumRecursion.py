def sum_of_numbers(num):
    if num == 0:
        return 0
    return num + sum_of_numbers(num - 1)


num = int(input("Enter a number: "))

print(sum_of_numbers(num))
