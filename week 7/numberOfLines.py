# this code calculates number of lines

def numberOflines(lines):
    print("Number of lines", len(lines))

file1 = open("numberOfLines.txt", "r")
numberOflines(file1.readlines())
file1.close()