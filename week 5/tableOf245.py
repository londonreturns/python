# this code prints multiplication of 2 4 5

numbers = (2, 4, 5)
temp = ""

for num in numbers:
    for i in range(1,11):
        temp = str(num) + " * " + str(i) + " = " + str(num * i)
        print(temp)
        temp = ""
