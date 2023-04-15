# this code counts how many times r is in month

def countR(file):
    for month in file:
        if "r" in month:
            countRInWord = 0
            for character in month:
                if "r" == character:
                    countRInWord += 1
            print(month.strip(), countRInWord)
        else:
            print(month.strip(), "0")


file1 = (open("month3Letter.txt", "r"))
countR(file1)
file1.close()