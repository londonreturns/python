# top items

def topThreeItems(maxItemsDic):
    maxItemsDic = (sorted(maxItemsDic.items(), key=lambda item: item[1]))
    print("Top three items are", maxItemsDic[2:5])


priceOfItem = {'item1': 45.50,
               'item2': 35,
               'item3': 41.30,
               'item4': 55,
               'item5': 24}

topThreeItems(priceOfItem)