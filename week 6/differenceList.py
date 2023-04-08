# this code computes the difference between two lists

def differenceList(listA, listB):
    listAB = []
    for listAelement in listA:
        if not listAelement in listB:
            listAB.append(listAelement)
    return (listAB)





list1 = ["red", "orange", "green", "blue", "white"]
list2 = ["black", "yellow", "green", "blue"]

print("Color1-Color2", differenceList(list1, list2))
print("Color2-Color1", differenceList(list2, list1))