# this code counts the number of vowels

# take input from user
input_string = input("Enter a string: ")

# initialise count
count = 0


for character in input_string:
    lowCharacter = character.lower()
    if lowCharacter == "a" or lowCharacter == "e" or lowCharacter == "i" or lowCharacter == "o" or lowCharacter == "u":
        count += 1


print("Number of vowels are", count)

