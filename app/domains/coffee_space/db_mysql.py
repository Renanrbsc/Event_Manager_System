from database.mysql_db.connect import DatabaseMySQL


class CoffeeRoomMySQL(DatabaseMySQL):
    __tablename__ = "coffee_spaces"

    def __init__(self):
        super().__init__()

    def get_all(self):
        sql = f"SELECT * FROM {self.__tablename__};"
        print(sql)
        coffee_spaces = super().get(script=sql)
        return coffee_spaces

    def get_by_id(self, id: str):
        sql = f"SELECT * FROM {self.__tablename__} WHERE id=%s;"
        print(sql, id)
        coffee_space = super().get(script=sql, id=id)
        return coffee_space

    def post(self, data: dict):
        sql = f"INSERT INTO {self.__tablename__} " \
              f"(id, name, capacity) " \
              f"VALUES (%s, %s, %s);"
        values: list = [data[key] for key in data]
        print(sql, values)
        coffee_space = super().insert(script=sql, values=values)
        return coffee_space

    def put_id(self, data: dict):
        sql = f"UPDATE {self.__tablename__} " \
              f"SET name=%s, capacity=%s " \
              f"WHERE id=%s;"
        values: list = [data[key] for key in data]
        values.append(values.pop(0))
        print(sql, values)
        coffee_space = super().update_id(script=sql, values=values)
        return coffee_space

    def remove_id(self, id: str):
        sql = f"DELETE FROM {self.__tablename__} " \
              f"WHERE id=%s;"
        print(sql, id)
        coffee_space = super().delete_id(script=sql, id=id)
        return coffee_space
