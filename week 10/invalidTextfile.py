try:
    with open ('temp2.txt', 'r') as file1:
        line = file1.readline()
except IOError:
    print("File not found")