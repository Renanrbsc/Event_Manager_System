class Tables:
    names: list = ["students", "event_rooms", "coffee_spaces"]

    def createTableStudents(self) -> str:
        return f"CREATE TABLE {self.names[0]}(" \
                "id varchar(4) NOT NULL," \
                "name varchar(50) NOT NULL," \
                "lastname varchar(100) NOT NULL," \
                "PRIMARY KEY (id));"

    def createTableEventRooms(self) -> str:
        return f"CREATE TABLE {self.names[1]}(" \
                "id varchar(4) NOT NULL," \
                "name varchar(100) NOT NULL," \
                "capacity varchar(3) NOT NULL," \
                "PRIMARY KEY (id));"

    def createTableCoffeeSpaces(self) -> str:
        return f"CREATE TABLE {self.names[2]}(" \
                "id varchar(4) NOT NULL," \
                "name varchar(100) NOT NULL," \
                "PRIMARY KEY (id));"
