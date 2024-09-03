# This program simulates a student management system
def create_student(name, id):
    student = {
        name,
        id
    }
    return student

def get_info_from_user():
    name = input("Enter your name:")
    id = input("Enter your id:")

    student = create_student(name, id);
    
    return student

# This will act like database
students = []
# This will help us determine whether to continue running app or not
response = ""

while response != "x":
    new_student = get_info_from_user()
    students.append(new_student)
    response = input("Enter x to stop otherwise any key to continue: ")

print(students)