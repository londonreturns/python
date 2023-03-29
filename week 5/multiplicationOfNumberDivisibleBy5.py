# this code prints multiplication of first 20 numbers divisible by 5

# initialising variable
product = 1

for i in range (1, 21):
    multipleOf5 = i * 5
    product *= multipleOf5

print("multiplication of first 20 numbers divisible by 5 are", product)