import uuid

def add_student(name, age):

    student_id = str(uuid.uuid4())

    student = {
        "id" : student_id,
        "name" : name,
        "age" : age
    }

    return student