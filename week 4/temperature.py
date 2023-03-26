# weather code

# take input from user
temperature = int(input("Enter temperature: "))
humidity = int(input("Enter humidity: "))

# checks the temperature and humidity
if temperature >= 85 and humidity > 60:
    # display output to user
    print("Muggy day today")
elif temperature >= 85:
    print("Warm, but not muggy today")
elif temperature >= 65:
    print("Pleasant today")
elif temperature <= 45:
    print("Cold today")
else:
    print("Cool today")