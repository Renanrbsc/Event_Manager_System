from database.mysql_db.connect import DatabaseMySQL


class EventRoomMySQL(DatabaseMySQL):
    __tablename__ = "event_rooms"

    def __init__(self):
        super().__init__()

    def get_all(self):
        sql = f"SELECT * FROM {self.__tablename__};"
        print(sql)
        event_rooms = super().get(script=sql)
        return event_rooms

    def get_by_id(self, id: str):
        sql = f"SELECT * FROM {self.__tablename__} WHERE id=%s;"
        print(sql, id)
        event_room = super().get(script=sql, id=id)
        return event_room

    def post(self, data: dict):
        sql = f"INSERT INTO {self.__tablename__} " \
              f"(id, name, capacity) " \
              f"VALUES (%s, %s, %s);"
        values: list = [data[key] for key in data]
        print(sql, values)
        event_room = super().insert(script=sql, values=values)
        return event_room

    def put_id(self, data: dict):
        sql = f"UPDATE {self.__tablename__} " \
              f"SET name=%s, capacity=%s " \
              f"WHERE id=%s;"
        values: list = [data[key] for key in data]
        values.append(values.pop(0))
        print(sql, values)
        event_room = super().update_id(script=sql, values=values)
        return event_room

    def remove_id(self, id: str):
        sql = f"DELETE FROM {self.__tablename__} " \
              f"WHERE id=%s;"
        print(sql, id)
        event_room = super().delete_id(script=sql, id=id)
        return event_room
