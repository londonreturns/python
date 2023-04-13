# this code check quotes(number and type)

file1 = (open("check_quotes.txt", "r"))

line = file1.read()
numOfSingleQuote = 0
numOfDoubleQuote = 0
for character in line:
    if character == "'":
        numOfSingleQuote += 1
    elif character == '"':
        numOfDoubleQuote += 1
if numOfSingleQuote % 2 == 0 and numOfDoubleQuote % 2 == 0:
    print(True)
else:
    print(False)

file1.close()