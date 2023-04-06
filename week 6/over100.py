# over 100

numbers = []

for i in range (0, 4):
    num = int(input("Enter a number: "))
    if num > 100:
        numbers.append("Over")
    else:
        numbers.append(num)

print(numbers)