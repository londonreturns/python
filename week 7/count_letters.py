# this code counts letters and put them in a tuple in a list

def count_letters(line1):
    result = []
    for i in range(len(line1)):
        if line1[i] == " ":
            continue
        tempTuple = ((line1[i]).lower(), line1.count(line1[i]))
        if not tempTuple in result:
            result.append(tempTuple)
    return result



file1 = (open("count_letters.txt", "r"))

line = file1.read()
print(count_letters(line))
file1.close()