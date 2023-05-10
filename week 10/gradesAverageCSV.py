import csv

path = 'grades.csv'

with open (path, 'r') as grade_file:
    lines = csv.reader(grade_file)
    all_students = list(lines)[1:]
    for student in all_students:
        average = format((int(student[1]) + int(student[2]) + int(student[3])) / 3,'.2f')
        print(f'{student[0]} {average}')
