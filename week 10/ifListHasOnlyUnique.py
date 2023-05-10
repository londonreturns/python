def has_only_unique(temp_list):
    for i in range(len(temp_list)):
        temp_list = temp_list[1:]
        if i in temp_list:
            return True
    return False


lis = [1, 2, 3, 4, 5, 6, 2]
print(has_only_unique(lis))