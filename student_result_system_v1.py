students = []
# 1ST FUNCTION
def add_student():
    name = input("Enter your name:")
    roll_no = int(input("Enter roll no:"))
    marks = int(input("Enter your marks:"))

    student = {
    "name": name,
    "roll_no": roll_no,
    "marks": marks
    }

    students.append(student)

#2ND FUNCTION
def view_students():
    if not students:
        print("No students registered")
    else:
        for student in students:
            print("Name:",student["name"],"Roll No:",student["roll_no"],"Marks:",student["marks"])
            grade = calculate_grade(student["marks"])
            print("Grade:",grade)
            print("-------------------------")

#3RD FUNCTION
def calculate_grade(marks):
    if marks > 100:
        return "Invalid Marks"
    elif marks < 0:
        return "Negative Marks is not allowed"
    elif marks >= 90 and marks <= 100:
        return "A"
    elif marks >= 80 and marks <= 89:
        return "B"
    elif marks >= 70 and marks <= 79:
        return "C"
    elif marks >= 60 and marks <= 69:
        return "D"
    elif marks <= 59:
        return "FAIL"
    
# 4TH FUNCTION
def search_student(roll_no):
    found = False
    for student in students:
        if roll_no == student["roll_no"]:
            print("Name:",student["name"],"Roll No:",student["roll_no"],"Marks:",student["marks"])
            grade = calculate_grade(student["marks"])
            print("Grade:",grade)
            
            found = True
            break
    
    if not found:
        print("Student not found")

# 5TH FUNCTION
def topper():
    print("===== TOPPER =====")
    if not students:
        print("No students registered")
        return
    top = students[0]
    for student in students:
       if top["marks"] < student["marks"]:
            top = student
    grade = calculate_grade(top["marks"])
    print(top["name"],"\n",top["roll_no"],"\n",top["marks"],"\n",grade)


# 6TH FUNCTION 
def class_statistics():
    if not students:
        print("No students registered")
        return
    total_students = len(students)
    top = students[0]
    for student in students:
       if top["marks"] < student["marks"]:
            top = student
    print("Highest Marks:",top["marks"])

#Lowest marks nikalna
    top = students[0]
    for student in students:
       if top["marks"] > student["marks"]:
            top = student
    print("Lowest Marks:",top["marks"])

# Average marks nikalna 
    total = 0
    for student in students:
        total += student["marks"]

    average = total / total_students
    print("Average Marks: ",average)

#Pass count aur fail count karna 
    passed_count = 0
    failed_count = 0
    for student in students:
        grade = calculate_grade(student["marks"])
        if grade == "FAIL":
            failed_count += 1
        else:
            passed_count += 1
    print("Passed Students: ",passed_count)
    print("Failed Students: ",failed_count)

#HANDLE MENU FUNCTION 
def handle_menu(choice):
    if choice == 1:
        add_student()

    elif choice == 2:
        view_students()

    elif choice == 3:
        print("Search Student")
        roll_no = int(input("Enter your Roll no: "))
        search_student(roll_no)

    elif choice == 4:
        topper()

    elif choice == 5:
        class_statistics()

    elif choice == 6:
        print("Thank you for using Student Result System.")
        

#Show Menu FUNCTION
def show_menu():
    print("===== Student Result System =====")
    print("1. Add Student\n2. View Students\n3. Search Student\n4. Topper\n5. Class Statistics\n6. Exit")
while True:
    show_menu()
    choice = int(input("Enter your choice:"))
    handle_menu(choice)
    
    if choice == 6:
        break
