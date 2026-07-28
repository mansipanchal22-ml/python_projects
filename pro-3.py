#pro-3 collecton manipulator

student = []
student_dict = {}

print("Welcome to Student Data Organizer!")

while True:

    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Student")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

# add student details 

    if choice == 1:

        print("\nEnter student details:")

        student_id = int(input("Student ID: "))
        name = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")
        subjects = input("Subjects (comma-separated): ")

    