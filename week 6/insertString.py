# this code inserts a string in front of elements

def addString(lst, strng):
    newList = []
    for number in lst:
        newElement = strng + str(number)
        newList.append(newElement)
        newElement = ""
    return newList

numList = [1, 2, 3, 4]
toAddString = "emp"


print(addString(numList, toAddString))