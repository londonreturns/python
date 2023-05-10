with open ('temp.txt', 'r') as file1:
    line = file1.readline()

word1 = input("which word do you want to change: ")
word2 = input("what do you want to change it to: ")

new_line = line.replace(word1, word2)

with open('temp.txt', 'w') as file2:
    file2.write(new_line)