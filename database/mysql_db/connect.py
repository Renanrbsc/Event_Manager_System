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

    def view_tables(self) -> list:
        self.cursor.execute(self.process.show_tables())
        return self.cursor.fetchall()

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
