# this code fomats name

def formatName(firstName, lastName):
    for i in range(min(len(firstName), len(lastName))):
        print( lastName[i].strip() + ", " + firstName[i].strip())



file1 = open("firstName.txt", "r")
file2 = open("lastName.txt", "r")

formatName(file1.readlines(), file2.readlines())

file1.close()
file2.close()