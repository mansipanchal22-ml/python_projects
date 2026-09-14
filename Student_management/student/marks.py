
from functools import reduce

def add_marks(student, marks):

    student['marks'] = marks

    return student

def calculate_total(marks):

    total = reduce(lambda x, y: x + y, marks)

    return total

def calculate_average(marks):

    total = calculate_total(marks)

    average = total / len(marks)

    return average