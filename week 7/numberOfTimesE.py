# this code counts how many times e is in a text file

def countE(file):
    count = 0
    for word in file:
        for character in word:
            if character == "e":
                count += 1
    print(count)


file1 = (open("original_text.txt", "r"))
countE(file1.readlines())
file1.close()