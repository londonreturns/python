# this code reduces spaces

def reduced_spaces(line):
    for i in range(len(line)):
        if i + 1 == len(line):
            break
        elif line[i] == " " and line[i + 1] == " ":
            line = line[:i] + line[i + 1:]
    print(line)

file1 = open("reduced_spaces.txt", "r")

reduced_spaces(file1.read())
file1.close()