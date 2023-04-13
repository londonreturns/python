# this code writes
file1 = open("datafile2.txt", "w")
file1.write("Hello World")
file1.close()
file1 = open("datafile2.txt", "r")
print(file1.readline())
file1.close()