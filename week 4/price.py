# this code calculates net amount

# take input from user
marked_price = int(input("Enter marked price: "))

# check amount of marked price and apply discount
if marked_price >= 10000:
    final_price = marked_price * .8
elif marked_price >= 5000:
    final_price = marked_price * .9
else:
    final_price = marked_price * .95

# display output to user
print("Your final price is", final_price)