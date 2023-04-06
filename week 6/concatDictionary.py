# concat dictionary

dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}

newDiction = {}

newDiction.update(dict1)
newDiction.update(dict2)
newDiction.update(dict3)

print(newDiction)
