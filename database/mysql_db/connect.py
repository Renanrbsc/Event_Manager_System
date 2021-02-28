import mysql.connector

from database.mysql_db.tables import Tables


class DatabaseMySQL:

    def __init__(self) -> None:
        self.connection = mysql.connector.connect(host="localhost",
                                                  user="user",
                                                  passwd="12345",
                                                  db="managerevent_db",
                                                  charset="utf8")
        self.cursor = self.connection.cursor()
        self.tables = Tables()

    def view_tables(self) -> list:
        self.cursor.execute(self.tables.show_all())
        return self.cursor.fetchall()

    def insert(self, script: str, values: list) -> str:
        self.cursor.execute(script, values)
        self.connection.commit()
        return f"{self.cursor.rowcount} Registro inserido."

    def get(self, script: str, id: str = None):
        if id:
            self.cursor.execute(script, (id,))
        else:
            self.cursor.execute(script)
        return self.cursor.fetchall()

    def update_id(self, script: str, values: list) -> str:
        self.cursor.execute(script, values)
        self.connection.commit()
        return f"{self.cursor.rowcount} Registro alterado."

    def delete_id(self, script: str, id: str):
        self.cursor.execute(script, (id,))
        return f"{self.cursor.rowcount} Registro deletado."

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
