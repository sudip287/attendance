def add_student():
    print("Adding a student...")

    roll_no = input("Enter student roll number: ")
    name = input("Enter student name: ")
    age = input("Enter student age: ")

    with open("students.txt", "a") as file:
        file.write(f"{roll_no},{name},{age}\n")
        print("Student data recorded successfully.")

def update_student():
    print("Updating a student...")

    roll_no = input("Enter the roll number of the student to update: ")
    updated_student_record=[]
    is_updated= False

    with open("students.txt", "r") as student_data:
        students= student_data.readlines()
        
        for student in students:
            student_record = student.strip()
            student_roll= student_record.split(",")
            
            if student_roll[0]== roll_no:
                print("Student record found",student_record)
                name = input("Enter student name: ")
                age = input("Enter student age: ")
                updated_student_record.append(f"{roll_no},{name},{age}\n")
                is_updated = True
            else:
                updated_student_record.append(student)
            
        if is_updated:
            with open("students.txt", "w") as file:
                    file.writelines(updated_student_record)
                    print("Student record added successfully")
        else:
            print(f"Student with {roll_no} does not exist")
                
def delete_student():
    print("Deleting a student...")

    roll_no = input("Enter the roll number of the student to delete: ")
    deleted_student_record=[]
    is_deleted= False
    
    with open("students.txt", "r") as student_data:
        students= student_data.readlines()
        
        for student in students:
            student_record = student.strip()
            student_roll= student_record.split(",")[0]
            
            if student_roll == roll_no:
                print("Student record found",student_record)
                is_deleted = True
            else:
                deleted_student_record.append(student)
            
        if is_deleted:
            with open("students.txt", "w") as file:
                    file.writelines(deleted_student_record)
                    print("STudent record added successfully")
        else:
            print(f"Student with {roll_no} does not exist")

def view_students():
    print("Viewing all students...")
    
    with open("students.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())