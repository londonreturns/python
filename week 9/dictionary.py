def value_of_key(dict1):
    try:
        choice = input('enter key: ')
        return dict1[choice]
    except KeyError:
        print('key not found')


value_of_key({
    'a':1, 'b':2, 'c':3, 
})