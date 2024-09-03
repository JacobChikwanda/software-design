# How do I create dictionaries in python
student = {
    "name": "John",
    "age": 20,
    "height": 5.6,
    "gender": 'M',
    "id": 120
}

student2 = {
    "name": "John",
    "age": 20,
    "height": 5.6,
    "gender": 'M',
    "id": 120
}

students = [
    student,
    student2
]

for s in students:
    print(s)

print(students)