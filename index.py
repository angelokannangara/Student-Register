def collect_student_info():
    name = input("Enter student's name: ")
    age = input("Enter student's age: ")
    grade = input("Enter student's grade: ")
    return f"{name}, {age}, {grade}"
def main():
    students = []
    
    while True:
        print("Student Registration System")
        student_data = collect_student_info()
        students.append(student_data)
        
        another = input("Do you want to register another student? (yes/no): ")
        if another.lower() != "yes":
            break
    
    # Save student data to a text file
    with open("student_data.txt", "w") as file:
        for student in students:
            file.write(student + "\n")

if __name__ == "__main__":
    main()
#created by angelo kannangara