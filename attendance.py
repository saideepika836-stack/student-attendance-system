print("==============================")
print("     STUDENT ATTENDANCE SYSTEM")
print("==============================")

students = []

while True:
    name = input("\nEnter student name: ")
    roll_no = input("Enter roll number: ")

    print("1. Present")
    print("2. Absent")

    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        status = "Present"
    elif choice == "2":
        status = "Absent"
    else:
        status = "Invalid choice"

    students.append([name, roll_no, status])

    more = input("\nDo you want to add another student? (yes/no): ")

    if more.lower() != "yes":
        break

print("\n========== ATTENDANCE REPORT ==========")

for student in students:
    print("Name:", student[0])
    print("Roll Number:", student[1])
    print("Attendance:", student[2])
    print("--------------------------------------")