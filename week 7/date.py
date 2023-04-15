# convert / to -

def converIntoDash(dateLine):
    for oneDay in dateLine:
        print(oneDay.replace("/", "-").strip())

date = open("date.txt", "r")
converIntoDash(date.readlines())
date.close()