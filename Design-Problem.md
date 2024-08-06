# Design Problem - Kopala Programmers School

The Kopala Programmers School needs a new system to track all of its students, professors, and courses. The system should:

- Track the courses offered, who teaches each course, and which students are enrolled in those courses.
- Track the grades of each student across all courses.
- Store the address, phone number, name, and age of each student and professor.

## Requirements

### Courses
- Each course has a maximum and minimum number of students that can enroll.
- Courses must be canceled if the minimum number of students is not reached.
- Each course is taught by at least one professor but sometimes may be taught by many.

### Professors
- Professors are salaried employees.
- Track the annual salary of professors.
- Professors receive a $20,000 bonus if they teach more than 4 courses in a semester.

### Students
- Students can be local or international.
- Students can be full-time or part-time (part-time if enrolled in less than 1 or 2 courses in a semester).
- A student can enroll in up to 6 courses at a time.
- Track grades for each course (numeric range: 0-100).
- Students with an average grade below 60% are on academic probation.

### System Reset
- The system will be reset and updated at the end of each semester.