# this code converts a list of multiple integer to a single integer

def listToInteger(numList):
    tempStr = ""
    for number in numList:
        tempStr += str(number)
    return int(tempStr)

print(listToInteger([11, 33, 50]))