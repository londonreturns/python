try:
    str_value = input("Enter number: ")
    if not str_value.isdigit():
        raise ValueError
    num = int(str_value)
    print(num)
except ValueError:
    print("error")