# this code prints multiplication table

while True:
    # take input from user
    num = int(input("Enter a positive number: "))

    # check if the number is positive
    if num > 0:
        # initiate loop
        for i in range(1, 11):
            print(num * i)
        break

