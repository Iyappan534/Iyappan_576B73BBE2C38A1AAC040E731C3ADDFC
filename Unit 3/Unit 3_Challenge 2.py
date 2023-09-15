def sort_students(students):
    # Sort the students based on cgpa in descending order
    students.sort(key=lambda x: x.cgpa, reverse=True)
    return students
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

    def __repr__(self):
        return f"Student(name={self.name}, roll_number={self.roll_number}, cgpa={self.cgpa})"

# Test cases
students = [
    Student("John Doe", "A101", 3.8),
    Student("Jane Smith", "A102", 3.9),
    Student("Sam Brown", "A103", 3.7)
]

sorted_students = sort_students(students)

for student in sorted_students:
    print(student)
