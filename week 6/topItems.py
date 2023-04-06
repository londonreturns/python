# top items

priceOfItem = {'item1': 45.50,
               'item2': 35,
               'item3': 41.30,
               'item4': 55,
               'item5': 24}

maxPrice = 0
maxItem = ""
for item, prices in priceOfItem.items():
    if maxPrice < prices:
        maxPrice = prices
        maxItem = item

print("Highest price item is", maxItem, maxPrice)