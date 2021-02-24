from app.domains.student.actions import StudentAction


class StudentView:

    def post(self):
        name = input("Digite o nome do estudante:")
        lastname = input("Digite o sobrenome do estudante:")
        student = StudentAction().create({"name": name,
                                          "lastname": lastname})
        return student

    def get_id(self):
        id = int(input("Digite o id(0,9999) do estudante:"))
        student = StudentAction().get(id)
        return student

    def get_all(self):
        students = StudentAction().get()
        return students

    def put(self):
        pass

    def delete(self):
        pass
