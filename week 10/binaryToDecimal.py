def bin_to_decimal(string_value):
    if string_value == '':
        return 0
    rest = string_value[:-1]
    least_significant = int(string_value[-1])
    digit = bin_to_decimal(rest)
    digit = (2 * digit) + least_significant
    return digit



num_in_string = input("Enter a number in binary: ")
print(bin_to_decimal(num_in_string))

