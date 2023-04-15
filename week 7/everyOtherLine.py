# this code writes every other line

def everyOtherLines(lines):
    with open("new_text.txt", "w") as new_text:
        allLines = lines.readlines()
        for i in range(len(allLines)):
            if (i + 1) % 2 == 1:
                new_text.write(allLines[i])


original_text = open("original_text.txt", "r")
everyOtherLines(original_text)
original_text.close()