# this code displays multiplication table

# defining multiplication table
def multiplication_table(n):
    # initialising temp
    temp1 = ""
    temp2 = ""
    for i in range(1, n + 1):
        temp2 += str(i) + "\t"
    print(temp2)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            temp1 += str(i * j) + "\t"
        print(temp1)
        temp1 = ""

# calling the multiplication_table function
multiplication_table(10)