# this code counts letters and put them in a tuple in a list

def count_letters(line):
    count = 0
    for character in line:
        if character == " " or character == "\n":
            continue
        else:
            count += 1

    print(count)

file1 = (open("countCharacters.txt", "r"))
line = file1.read()
count_letters(line)
file1.close()