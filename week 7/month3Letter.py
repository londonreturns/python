# month 3 letter

def monthLetter(file):
    for month in file:
        print(month[:3])

file1 = (open("month3Letter.txt", "r"))
monthLetter(file1)
file1.close()