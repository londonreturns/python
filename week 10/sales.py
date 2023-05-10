def calculate_units_sold(products):
    total_units = 0
    for product in products:
        this_units = int(product['UnitsSold'])
        total_units += this_units
    return total_units

def calculate_revenue(products):
    total_revenue = 0
    for product in products:
        product_revenue = int(product['UnitsSold']) * int(product['UnitPrice'])
        total_revenue += product_revenue
    return total_revenue

with open ('sales.txt', 'r') as file1:
    products = file1.readlines()

list_dic_products = []
for index, product in enumerate(products):
    temp_dic = {}
    if index == 0:
        keys = product.split(',')
    else:
        values = product.split(',')
        temp_dic[keys[0]] = values[0]
        temp_dic[keys[1]] = values[1]
        temp_dic[keys[2]] = values[2]
        temp_dic[keys[3]] = values[3]
        temp_dic[keys[4].strip()] = values[4]
        list_dic_products.append(temp_dic)

print('Total revenue is', calculate_revenue(list_dic_products))
print('Total units sold are', calculate_units_sold(list_dic_products))
