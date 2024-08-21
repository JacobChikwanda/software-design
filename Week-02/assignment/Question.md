# Assignment 2: Diagnosing and Improving a Student Management System

## Overview
In this assignment, you are tasked with analyzing and improving a simple Student Management System written in Python. The current system has several issues that violate key software design principles. Your job is to identify these issues, explain how they break the principles covered in Unit 2, and then refactor the code to align with best practices. Additionally, you'll be expected to enhance the user interaction by implementing a simple menu system that allows users to choose options like viewing student records, updating information, and more.

### Unit 2: Software Design Principles
- SOLID principles
- DRY (Don't Repeat Yourself)
- KISS (Keep It Simple Stupid)
- YAGNI (You Ain't Gonna Need It)

## Submission Link
[Kindly use this link to submit your work](https://forms.gle/8VaBPnemoazLFJo76)


## Scenario
You’ve been brought in as a consultant to review the Student Management System for a small educational institution. The system was developed quickly to meet immediate needs, but over time, several issues have emerged:

### User Feedback
- **Administrator Feedback:** "The system is functional, but whenever we request new features or changes, it takes a long time to implement. We've had to wait weeks for even simple updates."
- **IT Department Feedback:** "The codebase is difficult to maintain and scale. We've had several issues with bugs that are hard to trace because the logic is scattered everywhere."
- **New Developer Feedback:** "The code is hard to understand and lacks clear documentation. It’s challenging to figure out where to start when making changes."

## The Code
Below is the simplified version of the existing codebase. Your task is to analyze it and identify where it violates the software design principles from Unit 2. After your analysis, you will refactor the code to improve its design. You are also expected to enhance the system by adding a simple menu that allows users to interact with the system more effectively.

### student_management_system.py

```python
class Student:
    def __init__(self, id, name, age, major):
        self.id = id
        self.name = name
        self.age = age
        self.major = major

    def update_student(self, name=None, age=None, major=None):
        if name:
            self.name = name
        if age:
            self.age = age
        if major:
            self.major = major

    def display_student(self):
        print(f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Major: {self.major}")

class StudentDatabase:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        for student in self.students:
            if student.id == student_id:
                self.students.remove(student)
                break

    def display_all_students(self):
        for student in self.students:
            student.display_student()

class StudentManagementSystem:
    def __init__(self):
        self.database = StudentDatabase()

    def add_new_student(self, id, name, age, major):
        student = Student(id, name, age, major)
        self.database.add_student(student)

    def delete_student(self, student_id):
        self.database.remove_student(student_id)

    def update_student_info(self, student_id, name=None, age=None, major=None):
        for student in self.database.students:
            if student.id == student_id:
                student.update_student(name, age, major)

    def show_all_students(self):
        self.database.display_all_students()

# Example Usage
system = StudentManagementSystem()
system.add_new_student(1, "John Doe", 20, "Computer Science")
system.add_new_student(2, "Jane Smith", 22, "Mathematics")
system.show_all_students()
system.update_student_info(1, name="Johnathan Doe")
system.show_all_students()
system.delete_student(2)
system.show_all_students()
```

## Tasks

### 1. Analysis (30 points)
Identify the parts of the code that violate the following principles:
- **SOLID principles**
- **DRY (Don't Repeat Yourself)**
- **KISS (Keep It Simple Stupid)**
- **YAGNI (You Ain't Gonna Need It)**

Explain how each principle has been broken in the current code. Use specific examples from the code provided.

### 2. Refactoring (50 points)
Refactor the code to address the issues you identified in the analysis. Your refactored code should:
- Follow **SOLID principles**
- Eliminate redundancy (**DRY**)
- Simplify the design (**KISS**)
- Avoid unnecessary features or complexity (**YAGNI**)
- **Implement a Menu System:** Add a simple text-based menu that allows users to choose from options like adding a student, deleting a student, updating student information, and viewing all students.

### 3. Documentation (20 points)
Provide clear documentation for your refactored code. This includes:
- Comments explaining key sections of your code
- A README file in your GitHub repository that explains how to run the system and what changes were made.

## Submission Instructions
1. **Google Docs**: Submit a link to your Google Doc containing the analysis and documentation. Ensure that you have given edit access to `chikwajacobos@gmail.com`.
2. **GitHub Repository**: Create a GitHub repository for your refactored code. Include a README.md file that explains how to run the code. Submit the link to your repository along with your Google Docs link.

### Deadline
Please submit your assignment by **Tuesday, 27th 2024 before 12pm**.
