def products(numbers):
    if numbers == []:
        return 1
    num = numbers[0]
    rest = numbers[1:]
    product = products(rest)
    product = product * num
    return product
    
print('product is',products([5, 6, 2]))