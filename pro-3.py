listOfStudent = []

print("Welcome to Student Data Organizer!")


while True:

    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Student")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    selectOption = int(input("Enter Your Choice: "))

    if selectOption == 1:

        print("\nEnter Student Details")

        studentId = int(input("Enter Student ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        grade = input("Enter Grade: ")
        dob = input("Enter DOB (YYYY-MM-DD): ")
        subject = input("Enter Subjects (comma separated): ").split(",")

        subject = [i.strip() for i in subject]
        studentTuple = (studentId, dob)
        subjectSet = set(subject)
        studentDictionary = {
                        "studentOfTuple": studentTuple,
                        "id": studentId,
                        "name": name,
                        "age": age,
                        "Grade": grade,
                        "subject": subjectSet
        }

        listOfStudent.append(studentDictionary)

        print("Student Added Successfully")

    elif selectOption == 2:

        print("\n------ Student List ------")

        if len(listOfStudent) == 0:
            print("No Student Found")

        else:

            for student in listOfStudent:

                print(f"""
                        Student ID : {student['studentOfTuple'][0]}
                        DOB        : {student['studentOfTuple'][1]}
                        Name       : {student['name']}
                        Age        : {student['age']}
                        Grade      : {student['Grade']}
                        Subjects   : {', '.join(student['subject'])}
                    """)

    elif selectOption == 3:

        studentIdToUpdate = int(input("Enter Student ID: "))

        isMatch = False

        for i in range(len(listOfStudent)):
            if listOfStudent[i]["id"] == studentIdToUpdate:

                isMatch = True

                oldSubject = input("Enter Subject To Update: ")
                newSubject = input("Enter New Subject: ")
                listOfSubject = list(listOfStudent[i]["subject"])

                if oldSubject in listOfSubject:

                    index = listOfSubject.index(oldSubject)
                    listOfSubject[index] = newSubject
                    listOfStudent[i]["subject"] = set(listOfSubject)

                    print("Subject Updated Successfully")

                break

    elif selectOption == 4:

        studentIdToDelete = int(input("Enter Student ID: "))

        isMatch = False

        for i in range(len(listOfStudent)):
            if listOfStudent[i]["id"] == studentIdToDelete:

                del listOfStudent[i]
                isMatch = True

                print("Student Deleted Successfully")

                break

    elif selectOption == 5:

        allSubjects = set()

        for student in listOfStudent:
             allSubjects.update(student["subject"])

        print("\nSubjects Offered")

        for sub in allSubjects:
            print(sub)

    elif selectOption == 6:

        print("Thank You For Using Student Data Organizer")

        break

    else:

        print("Invalid Choice")