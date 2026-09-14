from .marks import add_marks, calculate_total, calculate_average

def add_result(student):

    student["total"] = calculate_total(student["marks"])

    student["average"] = calculate_average(student["marks"])

    return student

def get_names(students):

    names = list(
        map(lambda student: student["name"], students)
    )

    return names

def filter_students(students, minimum_marks):

    result = list(
        filter(
            lambda student: student["average"] >= minimum_marks,students
        )
    )

    return result

def sort_students(students):

    result = sorted(
        students, key=lambda student: student["average"], reverse = True
    )

    return result