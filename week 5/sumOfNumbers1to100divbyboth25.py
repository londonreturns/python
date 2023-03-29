# this program calculate the sum of all numbers between 1 and 100 that are not divisible by 3 or 5 using a loop

# initiate variable
sum = 0

# start loop
for i in range(1, 101):
    if i % 3 != 0 or i % 5 != 0:
        sum += i

print(sum)
