# this code extracts number from a string

file1 = (open("extract_temp.txt", "r"))
wordList = file1.read().split(" ")
for word in wordList:
    if word.isdigit():
        print(word)


file1.close()