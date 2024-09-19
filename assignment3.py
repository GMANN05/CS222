def student_list(file_name):
    students = {}
    with open(file_name, 'r') as file:
        for line in file:
            
            student_info = line.strip().split(',')
            student_id = student_info[0]
            last_name = student_info[1]
            first_name = student_info[2]
            major = student_info[3]
            gpa = student_info[4]
            
            students[student_id] = [last_name, first_name, major, gpa]
    return students  

def searchLN(students, last_name):
    print(f"\nStudents with last name '{last_name}'")
    found = False
    for student_id, data in students.items():
        if data[0].lower() == last_name.lower():
            print(f"ID: {student_id}, Last Name: {data[0]}, First Name: {data[1]}, Major: {data[2]}, GPA: {data[3]}")
            found = True
    if not found:
        print(f"No students found with that last name.")

def searchM(students, major):
    print(f"\nStudents with major '{major}':")
    found = False
    for student_id, data in students.items():
        if data[2].lower() == major.lower():
            print(f"ID: {student_id}, Last Name: {data[0]}, First Name: {data[1]}, Major: {data[2]}, GPA: {data[3]}")
            found = True
    if not found:
        print(f"No students found with that major.")

def main():
    students = student_list('students.txt')
    while True:
        print("\nChoose an option:")
        print("1) Search by Last Name")
        print("2) Search by Major")
        print("3) Quit")

        user = input("Select an option: ")

        if user == '1':
            last_name = input("Enter the student's last name you want to search for: ")
            searchLN(students, last_name)
        elif user == '2':
            major = input("Enter the student's major you want to search for: ")
            searchM(students, major)
        elif user == '3':
            break
        else:
            print("Invalid choice, please choose one of the three options above.")

main()
