students = []

def add_student():
    """
    TODO: Prompt the user to enter student name, age, and grade.
    Append the student as a dictionary to the students list.
    """
    name=input("insert student name: ")
    age = int(input("Enter student's age: "))
    grade = float(input("Enter student's grade: "))
    
    # Create a dictionary for the new student
    student={
        "name": name,
        "age" : age,
        "grade": grade
    }
    students.append(student)
    print(f"✅ Student '{name}' added successfully!") 

    

def view_students():
    """
    TODO: Loop through the students list and print each student's info.
    """
    for student in students:
        print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
    

def get_average_grade():
    """
    TODO: Return the average grade of all students.
    """
    """Calculates the average of all grades."""
    if not students:
        print("\n--- No students to calculate average.\n")
        return

    total = sum(s["grade"] for s in students)
    avg = total / len(students)
    print(f"\n📊 Average Grade: {avg:.2f}\n") 
    