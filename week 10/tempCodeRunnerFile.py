th open('temp.txt', 'r') as file:
    line = file.readline()
    words = line.split(' ')
    frequency_of_