import os
from datetime import date

def take_attendance():
    with open("students.txt","r") as file:
        students_data = file.readlines()
        student_attendance=[]
        for student in students_data:
            student=student.strip()
            roll = student.split(",")[0]
            name = student.split(",")[1]
            while True:
                print(roll,name)
                attendance = input("Present (y/n)").lower()
                if attendance == "y" or attendance == "n":
                    student_attendance.append(f"{roll},{name},{attendance}\n")
                    break
                else:
                    print("Enter Valid input")
    with open(f"attendance/{date.today()}.txt","w") as file:
        file.writelines(student_attendance)
                    
def view_attendance():
    date_input = input("Enter the date (yyyy-dd-mm) of the attendance:")
    if os.path.exists(f"attendance/{date_input}.txt"):
        with open(f"attendance/{date_input}.txt","r") as file:
            attendence_data=file.readlines()
            for attendence in attendence_data:
                print(attendence.strip())
    else:
        print("File Does not Exist")