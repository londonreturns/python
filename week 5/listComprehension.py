# list comprehension

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


newList = [x**2 if x % 2 ==0 else x for x in lst]
print(newList)