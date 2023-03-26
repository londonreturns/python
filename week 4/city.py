# prompting user to input city
city = input("Enter the city ").lower()

# using nested if to display monuments'
if city == "Kathmandu" or city == "ktm" or city == "k":
    print("Pashupatinath Temple ")
elif city == "Pokhara" or city == "pkh" or city == "p":
    print("Fewa lake")
elif city == "Nepalgunj" or city == "npj" or city == "n":
    print("Bageshowri Temple")
elif city == "Birgunj" or city == "bnj" or city == "b":
    print("Birgunj Ghanta Ghar")

