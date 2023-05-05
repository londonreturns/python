def add_new_student():
    while True:
        try:
            name_marks = input('Student name, marks: ')
            name_marks_li = name_marks.split(',')
            name = name_marks_li[0]
            mark = float(name_marks_li[1])
            return name.strip(), float(mark)
        except ValueError:
            print('input is invalid')
        except IndexError:
            print('inappropiate amount of values')

stu_dict = {}
while True:
    try:
        number_of_students = int(input('Enter number of students: '))
        while True:
            for i in range(number_of_students):
                student, marks = add_new_student()
                stu_dict[student] = marks
            break
        break
    except ValueError:
        print('error')

all_students = []
total_marks = 0
count = 0
for key, value in stu_dict.items():
    all_students.append(key)
    total_marks += value
    count += 1

print('average', format(total_marks / count,".2f"))
print(all_students)