try:
    amount = int(input("Enter amount: "))
    if amount < 10000:
        raise ValueError
except ValueError:
    print('error less than 10000')