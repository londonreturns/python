# if key value exists

def ifKeyValueExists(studs, keyQuery, valueQuery):
    isFound = False
    for keyValue in studs:
        for key, value in keyValue.items():
            if keyQuery.lower() == key.lower() and valueQuery == value:
                isFound = True
                print("Key:", keyQuery, "and Value:", valueQuery, "exists")
                break
    if not isFound:
        print("Key:", keyQuery, "and Value:", valueQuery, "does not exists")

students = [
            {"student_id": 1, "name": "Jean Castro", "class": "V"},
            {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'},
            {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'},
            {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'},
            {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}
]

ifKeyValueExists(students, "name", "Jean Castro")
ifKeyValueExists(students, "address", "New York")