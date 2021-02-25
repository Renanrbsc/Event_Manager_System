from app.domains.student.models import Student
from database.mysql_db.connect import DatabaseMySQL
from database.mysql_db.tables import Tables


class StudentActionMySQL:

    def __init__(self):
        self.db = DatabaseMySQL()
        self.db.start_connector()

    def create(self, data: dict):
        student = Student(name=data["name"],
                          lastname=data["lastname"])
        print(self.db.get_id(table=Tables.names[0], id=student.getId()))
        if not self.db.get_id(table=Tables.names[0], id=student.getId()):
            self.db.create_data(table=Tables.names[0], data=student.serialize())
            return student.serialize()
        else:
            return f"{str(student)}" \
                    "Unsaved record."

    def update(self):
        pass

    def delete(self):
        pass

    def get(self, id: int = None):
        if id:
            student = Student(id=id)
            students = self.db.get_id(table=Tables.names[0], id=student.getId())
        else:
            students = self.db.get_all(table=Tables.names[0])
        print(f"{len(students)} found.")
        return students
