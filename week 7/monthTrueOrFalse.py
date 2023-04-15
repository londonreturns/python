# month 3 letter

def monthTrueOrFalse(file):
    for month in file:
        if "r" in month:
            print(True)
        else:
            print(False)

file1 = (open("month3Letter.txt", "r"))
monthTrueOrFalse(file1)
file1.close()