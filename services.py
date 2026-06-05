def add_student (database, student):
    database.append(student)

def get_all_students (database):
    return database

def find_student (database, nom):
    for student in database:
        if student ["nom"] == nom:
            return student
    return None 

def calculate_average (student):
    notes = student ["notes"]
    return sum(notes) / len(notes)