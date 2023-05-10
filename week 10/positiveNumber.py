try:
    num = int(input("Enter a number: "))
    if num < 0:
        raise ValueError
except ValueError:
    print("please enter positive value")