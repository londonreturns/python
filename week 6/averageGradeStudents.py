# average grade for each students

def averageGrades(allStudents):
    sum = 0
    for student in allStudents:
        for grade in student["grades"]:
            sum += grade
        print(student["name"] + ":",  format((sum / 3), ".1f"))
        sum = 0


students = [
    {"name": "Alice", "age": 17, "gender": "female", "grades": [90, 85, 95]},
    {"name": "Bob", "age": 16, "gender": "male", "grades": [80, 75, 70]},
    {"name": "Charlie", "age": 16, "gender": "male", "grades": [100, 90, 95]},
    {"name": "Diana", "age": 17, "gender": "female", "grades": [85, 80, 90]},
    {"name": "Emily", "age": 16, "gender": "female", "grades": [95, 90, 100]}
]

averageGrades(students)
