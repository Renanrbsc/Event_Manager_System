from database.mysql_db.connect import DatabaseMySQL


class StudentMySQL(DatabaseMySQL):
    __tablename__ = "students"

    def __init__(self):
        super().__init__()

    def get_all(self):
        sql = f"SELECT * FROM {self.__tablename__};"
        print(sql)
        students = super().get(script=sql)
        return students

    def get_by_id(self, id: str):
        sql = f"SELECT * FROM {self.__tablename__} WHERE id=%s;"
        print(sql, id)
        student = super().get(script=sql, id=id)
        return student

    def post(self, data: dict):
        sql = f"INSERT INTO {self.__tablename__} " \
              f"(id, name, lastname) " \
              f"VALUES (%s, %s, %s);"
        values: list = [data[key] for key in data]
        print(sql, values)
        student = super().insert(script=sql, values=values)
        return student

    def put_id(self, data: dict):
        sql = f"UPDATE {self.__tablename__} " \
              f"SET name=%s, lastname=%s " \
              f"WHERE id=%s;"
        values: list = [data[key] for key in data]
        values.append(values.pop(0))
        print(sql, values)
        student = super().update_id(script=sql, values=values)
        return student

    def remove_id(self, id: str):
        sql = f"DELETE FROM {self.__tablename__} " \
              f"WHERE id=%s;"
        print(sql, id)
        student = super().delete_id(script=sql, id=id)
        return student
