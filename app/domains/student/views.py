from app.domains.student.action_mysql import StudentActionMySQL


class StudentView:

    def __init__(self):
        self.action = StudentActionMySQL()

    def post(self):
        name = input("Digite o nome do estudante:")
        lastname = input("Digite o sobrenome do estudante:")
        student = self.action.create({"name": name,
                                      "lastname": lastname})
        return student

    def get_id(self):
        id = int(input("Digite o id(0,9999) do estudante:"))
        student = self.action.get(id)
        return student

    def get_all(self):
        students = self.action.get()
        return students

    def put_id(self):
        id = int(input("Digite o id(0,9999) do estudante:"))
        name = input("Digite o novo nome do estudante:")
        lastname = input("Digite o novo sobrenome do estudante:")
        student = self.action.update_id({"name": name,
                                         "lastname": lastname}, id)
        return student

    def delete_id(self):
        id = int(input("Digite o id(0,9999) do estudante:"))
        student = self.action.delete_id(id)
        return student
