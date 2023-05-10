with open('temp.txt', 'r') as file1:
    line = file1.readline()
    words = line.split(' ')


print(line)
count = 0
for word in words:
    if word[0].lower() in ('a', 'e', 'i', 'o', 'u'):
        count += 1

print(count)
