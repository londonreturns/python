# this code takes in a list of strings and returns list with only the strings that have 'a'

# defining function
def onlyStringWithA(lst):
    newList = []
    for item in lst:
        for character in item.lower():
            if character == "a":
                newList.append(item)
                break
    return newList

lst = ["asd", "sdf", "qaa"]
print(onlyStringWithA(lst))