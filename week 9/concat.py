def concat(str1, str2):
    try:
        return str1 + str2
    except TypeError:
        print('error, is not string')
        
        
concat('abc', 123)