# this code returns the product of the two if any is negative return 0
# defining function product
def product(n1, n2):
    # check if the numbers are postive
    if n1 > 0 and n2 > 0:
        # return product
        return n1 * n2
    else:
        # return 0
        return 0

# take input from user
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

# call function and print output
print("The product is", product(num1, num2))
