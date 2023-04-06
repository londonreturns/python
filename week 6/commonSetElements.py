# this code calculates intersection of 2 sets

def sameElements(set1, set2):
    newSet = set()
    for element in set1:
        if element in set2:
            newSet.add(element)
    return newSet


setA = {1, 2, 3, 4, 5}
setB = {7, 8, 3, 4, 5}
print(sameElements(setA, setB))