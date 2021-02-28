from app.domains.student.models import Student
from app.domains.student.db_mysql import StudentMySQL


class StudentActionMySQL:

    def __init__(self):
        self.db = StudentMySQL()

    def create(self, data: dict):
        student = Student(name=data["name"],
                          lastname=data["lastname"])
        if not self.db.get_by_id(id=student.getId()):
            row = self.db.post(data=student.serialize())
            return f"{student.serialize()}\n{row}"
        else:
            return f"{student.serialize()}\nRegistro não salvo."

    def update_id(self, data: dict, id: int):
        student = Student(id=id,
                          name=data["name"],
                          lastname=data["lastname"])
        if self.db.get_by_id(id=student.getId()):
            row = self.db.put_id(data=student.serialize())
            return f"{student.serialize()}\n{row}"
        else:
            return f"{student.serialize()}\nRegistro não encontrado."

    def delete_id(self, id: int = None):
        student = Student(id=id)
        if self.db.get_by_id(id=student.getId()):
            return self.db.remove_id(id=student.getId())
        else:
            return f"Registro não encontrado."

    def get(self, id: int = None):
        if id:
            student = Student(id=id)
            students = self.db.get_by_id(id=student.getId())
        else:
            students = self.db.get_all()
        print(f"{len(students)} encontrado(s).")
        return students
