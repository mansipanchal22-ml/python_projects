from student.details import add_student
from student.marks import add_marks
from student.operations import add_result, get_names, filter_students, sort_students


def main():

    students = []
    student1 = add_student("Man", 20)

    add_marks(student1, [56, 45, 67])

    add_result(student1)

    #student 2
    student2 = add_student("Ahan", 22)

    add_marks(student2, [78, 67, 88])
    add_result(student2)

    #student3
    student3 = add_student("aliza", 21)

    add_marks(student3, [45, 56, 67])
    add_result(student3)

    students.append(student1)
    students.append(student2)
    students.append(student3)

    print("\n all students")

    for student in students:
        print("\nID :", student["id"])
        print("name :", student["name"])
        print("age :", student["age"])
        print("marks :", student["marks"])
        print("total :", student["total"])
        print("average :", student["average"])

    #map

    names = get_names(students)

    for name in names:

        print("\n name :", name)

    #filter

    filtered_students = filter_students(students, 80)

    for student in filtered_students:

        print(
            student["name"],

            student["average"]

        )

    #sorted()

    sorted_students = sort_students(students)

    for student in sorted_students:

        print(
            student["name"],

            student["average"]

        )

if __name__ == "__main__":
    main()