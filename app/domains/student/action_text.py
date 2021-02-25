from app.domains.student.models import Student
from database.text_db.process import read_id, read_all, append_model


class StudentActionText:

    def create(self, data: dict):
        student = Student(name=data["name"],
                          lastname=data["lastname"])

        if not read_id(local_name="student", model=student):
            append_model(local_name="student", model=student)
            return student
        else:
            return f"Registro não salvo!\n"

    def update(self):
        pass

    def delete(self):
        pass

    def get(self, id: int = None):
        if id:
            students = read_id(local_name="student", model=Student(id=id))
        else:
            students = read_all(local_name="student")
        return students
