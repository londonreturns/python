# this code displays multiplication / exponent table
# defining multiplication table
def multiplication_table(n, isTrue):
    # initialising temporary
    temp1, temp2 = "", ""
    # loop to print first line
    for i in range(1, n + 1):
        temp2 += "\t" + str(i)
    # display first line
    print(temp2)
    # loop to create rows
    for i in range(1, n + 1):
        # assigning first value to string
        temp1 += str(i) + "\t"
        # loop to create columns
        for j in range(1, n + 1):
            if not isTrue:
                # assigning column values to string
                temp1 += str(i * j) + "\t"
            else:
                # assigning column values to string
                temp1 += str(i ** j) + "\t"
        # display all values
        print(temp1)
        temp1 = ""
# calling the multiplication_table function
multiplication_table(3, True)
