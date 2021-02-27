import mysql.connector

from database.mysql_db.tables import Tables
from database.mysql_db.process import Process


class DatabaseMySQL:

    def __init__(self) -> None:
        self.connection = None
        self.cursor = None
        self.process = Process()
        self.tables = Tables()

    def start_connector(self) -> None:
        self.connection = mysql.connector.connect(host="localhost",
                                                  user="user",
                                                  passwd="12345",
                                                  db="managerevent_db",
                                                  charset="utf8")
        self.cursor = self.connection.cursor()
        return self.cursor

    def view_tables(self) -> list:
        self.cursor.execute(self.process.show_tables())
        return self.cursor.fetchall()

    def create_data(self, table: str, data: dict) -> None:
        columns_list = [column for column in data.keys()]
        values_list = [data[key] for key in data]
        script = self.process.insert_into(table=table, columns=columns_list)

        self.cursor.execute(script, values_list)
        self.connection.commit()
        print(self.cursor.rowcount, "Record inserted.")

    def get_id(self, table: str, id: str):
        self.cursor.execute(self.process.select_id(table=table), (id,))
        record = self.cursor.fetchall()
        return record

    def get_all(self, table: str):
        self.cursor.execute(self.process.select_all(table=table))
        records = self.cursor.fetchall()
        return records

    def put_id(self, table: str, data: dict) -> None:
        columns_list = [column for column in data.keys()]
        values_list = [data[key] for key in data]
        value_id = values_list.pop(0)
        script = self.process.update_id(table=table, columns=columns_list)
        print(script, values_list.append(value_id))
        self.cursor.execute(script, values_list.append(value_id))
        self.connection.commit()
        print(self.cursor.rowcount, "Record inserted.")

    def start_tables(self) -> None:
        tables_db = self.view_tables()

        if not (self.tables.names[0],) in tables_db:
            self.cursor.execute(self.tables.createTableStudents())
        if not (self.tables.names[1],) in tables_db:
            self.cursor.execute(self.tables.createTableEventRooms())
        if not (self.tables.names[2],) in tables_db:
            self.cursor.execute(self.tables.createTableCoffeeSpaces())

        tables_db = self.view_tables()
        print(f"{len(tables_db)} tables in database MySQL: "
              f"{', '.join( [name for (name,) in tables_db] )}"
              f"\n")
