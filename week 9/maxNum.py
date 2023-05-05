def maxNum(lst):
    try:
        if len(lst) == 0:
            raise ValueError
        max_num = 0
        for num in lst:
            if max_num < num:
                max_num = num
        return max_num
    except ValueError:
        print('empty list')

print(maxNum([]))