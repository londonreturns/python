# this code gets the largest number

# initialising variables
numbers = [1, 2, 3, 4, 5, 6]
largest = 0

for number in numbers:
    if largest < number:
        largest = number

print("Largest is", largest)