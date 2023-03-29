# this code adds up all the even numbers between 100 and 200, inclusive

# initiate variable
count = 100
sum = 0

while True:
    if count % 2 == 0 and 100 <= count <= 200:
        sum += count
        count += 1
    elif count > 200:
        break
    elif count % 2 != 0:
        count += 1
        continue

print("Sum is", sum)